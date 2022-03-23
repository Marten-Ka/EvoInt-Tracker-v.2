import sys
from collections import OrderedDict
from urllib.request import urlopen
import urllib.parse
from urllib.parse import urlparse
import os
from pathlib import Path
from bs4 import BeautifulSoup
from time import time

from pdf2image import convert_from_path
from urllib.error import HTTPError

from Publication import publications, Publication, get_keywords_from_csv
from Vikus_writer import create_data_csv, read_data_csv, add_to_data_csv, clear_data_csv, get_last_publication_link, get_last_valid_publication, get_last_valid_publication_link, get_publication_information_by_link, close_csv_file_reader
from Year import years, Year

#
# Every n downloads the progress will be printed.
# If None every single download the progress will be printed.
# 
PRINT_PROGRESS_STEP = None

IJCAI_URL = "https://www.ijcai.org/past_proceedings/"

VIKUS_VIEWER_PATH = "../vikus-viewer/"

VIKUS_VIEWER_DATA_PATH = VIKUS_VIEWER_PATH + "data/"
VIKUS_VIEWER_DATA_IMAGES_PATH = VIKUS_VIEWER_DATA_PATH + "images/"

VIKUS_VIEWER_DATA_FULLTEXT_PATH = VIKUS_VIEWER_DATA_PATH + "fulltext/"
VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH = VIKUS_VIEWER_DATA_FULLTEXT_PATH + "pdf/"

def parse_title(title):
    #title = title.replace('\n', ' ')
    #title = title.replace('\t', ' ')
    #title = title.replace('  ', ' ')
    #title = title.strip()
    return title.replace('\n', ' ').replace('\t', ' ').replace('  ', ' ').strip()

# searches for the next available id
def next_pub_id():
    ids = [int(pub_id) for pub_id in publications.keys()]
    ids.sort()
    result = str(ids[-1] + 1) if len(ids) > 0 else '0'
    return result.zfill(4)

def get_id_from_link(link):
    id = link.split('/')  # https://www.ijcai.org/proceedings/2020/0085.pdf
    id = id[len(id) - 1]  # 0085.pdf
    id = id[0:id.find('.')] # 0085
    return id
    
        
def download_publication(publication):
    
    #
    # If PDF already exists -> don't download again
    # unless it has a size of 0
    #
    if Path(publication.get_path_to_pdf()).is_file():
        
        #
        # We need to check if the file size is
        # greater than zero, because then the file
        # could not be downloaded properly.
        # For example when exiting the script when downloading.
        #
        file_size = os.path.getsize(publication.get_path_to_pdf())
        if file_size > 0:
            return
        
        return
    
        
    try:
        #print(f'Downloading publication "{publication.title}" \n\t\tfrom {publication.origin_path}\n')
        response = urlopen(publication.get_pdf_link())
        # TODO: path_to_pdf has to start at data/..., so add vikus-viewer/ here
        os.makedirs(publication.get_path_to_pdf()[:-8], exist_ok=True)
        file = open(publication.get_path_to_pdf(), 'wb')
        file.write(response.read())
        file.close()
    except HTTPError:
        print("Error writing file: " + publication.get_pdf_link())
    except TimeoutError:
        print("TimeoutError")

def is_link_to_volume(link: str):
    year = link.split("/")[-1]
    if not year:
        year = link.split("/")[-2]
    # print(year)
    return year[:4].isdigit()

#
# Parses every available year in the given URL.
# Returns a sorted set (starting with "newest" year)
#

def get_available_volumes():
    
    result = set()
    
    response = urlopen(IJCAI_URL)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find('div', 'content')
    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link.split("/")[-1] == "2017":
            current_link = current_link + "/"
        if is_link_to_volume(current_link):
            if current_link not in result:
                result.add(current_link)
    return sorted(result, reverse=True)

def download_from_single_volume_years():
    
    if not Path(VIKUS_VIEWER_DATA_PATH + "data.csv").is_file():
        with open(VIKUS_VIEWER_DATA_PATH + "data.csv", "w") as f: # create file
            pass

    # clear_data_csv()
    
    # last available data from publication
    last_publication_link = get_last_publication_link()
    last_publication_reached = False
    
    pdf_count_0722 = 0

    base_pdf_path = VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH

    available_volumes = get_available_volumes()
    #print('\n'.join(available_volumes))

    for volume_link in available_volumes:
        year = volume_link.split("/")[-1][:4]
        if not year:
            year = volume_link.split("/")[-2][:4]
        Year(year)
        os.makedirs(base_pdf_path + year, exist_ok=True)

        visited_links = []
        # year_url = urllib.parse.urljoin(base_url, year)
        response = urlopen(volume_link)  # opens the URL
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        print(f'[{year}] - Parsing website ({volume_link})...')
        for link in soup.find_all('a'):
            current_link = link.get('href')
            
            if volume_link not in current_link:
                current_link = urllib.parse.urljoin(volume_link, current_link)
            if current_link.endswith('.pdf') and current_link not in visited_links:
                visited_links.append(urllib.parse.urljoin(volume_link, current_link))

                if not urlparse(current_link).scheme:
                    current_link = 'https://' + current_link
                
                publication_id = next_pub_id()
                #publication_id = get_id_from_link(current_link)
                
                title = parse_title(link.text)
                if title == "here" or current_link == f'https://www.ijcai.org/proceedings/{year}/preface.pdf':
                    continue

                authors = ""

                # TODO: Following lines in own Method. Check if link is actually a publication.
                if title == "PDF":  # TODO: missing for years 2015, 2016
                    if int(year) >= 2017:
                        paper_wrapper = link.find_parent("div", "paper_wrapper")
                        title = paper_wrapper.find("div", "title")
                        title = parse_title(title.text)
                        authors = paper_wrapper.find("div", "authors").text
                
                #
                # Skip the first entry with this title,
                # because it is an duplicate of the last entry.
                # This is an error on the website.
                #
                if title == "Self-Adaptive Swarm System (SASS)":
                    pdf_count_0722 += 1
                    if pdf_count_0722 == 1:
                        continue
                    
                last_publication_reached = create_publication(last_publication_reached, get_last_publication_link, publication_id, year, title, authors, current_link)
                    
        print(f'[{year}] - Loaded and downloaded all PDFs!')

    #create_data_csv(publications)

def create_publication(last_publication_reached, get_last_publication_link, publication_id, year, title, authors, current_link):
    
    #
    # If the last publication, which is in the data.csv, was already reached, then we can only
    # download the next publications.
    # Because of that, we don't need to download publications, we already downloaded.
    #
    
    publication = None
    
    if last_publication_reached:
        publication = create_new_publication(publication_id, title, authors, year, current_link)
    else:
        
        #
        # We try to create a publication from the data in the data.csv.
        # If it fails, because the data row was not found, we create the
        # publication with the link.
        #
        
        publication = create_available_publication(current_link, year)
        
        if publication == None:
            publication = create_new_publication(publication_id, title, authors, year, current_link)

    if get_last_publication_link == current_link:
        last_publication_reached = True
        close_csv_file_reader()
    
    return last_publication_reached

#
# Tries to create a publication object from data.csv-entry
# Returns if data was available
#
def create_available_publication(current_link, year):
    
    data_row = get_publication_information_by_link(current_link)
    
    if data_row == None:
        return None
    else:

        if(PRINT_PROGRESS_STEP == None or (int(data_row.id) % PRINT_PROGRESS_STEP == 0)):
            print(f'[{year}] - [{data_row.id}] Creating publication "{data_row.get_encoded_title()}" (from data.csv) [{current_link}]')
        
        publication = create_publication_object(data_row.id, data_row.title, data_row.authors, data_row.year, data_row.get_pdf_link())
        return publication

#
# Creates a publication object from a link
#
def create_new_publication(publication_id, title, authors, year, current_link):

    encoded_title = title.encode('utf8')
    if(PRINT_PROGRESS_STEP == None or (int(global_id) % PRINT_PROGRESS_STEP == 0)):
        print(f'[{year}] - [{publication_id}] Creating publication "{encoded_title}" (from {current_link})')

    publication = create_publication_object(publication_id, title, authors, year, current_link)
    
    download_publication(publication)

    add_to_data_csv(publication)
    pdf_to_thumbnail(publication)
    
    return publication
    
def create_publication_object(publication_id, title, authors, year, current_link):
    path_to_pdf = VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH + str(year) + '/' + str(publication_id) + '.pdf'
    return Publication(publication_id=publication_id,
                        title=title,
                        authors=authors,
                        year=year,
                        origin_path=current_link,
                        path_to_pdf=path_to_pdf)

# Create thumbnail for multiple publications
def pdfs_to_thumbnail(dct):
    for publication in dct.values():
        pdf_to_thumbnail(publication)

# TODO: actually use var output_path on save
# Create thumbnail for one publications
def pdf_to_thumbnail(publication):

    directory_path = 'data/thumbnails'

    # Create thumbnail folder if it does NOT exist
    Path(directory_path).mkdir(parents=True, exist_ok=True)

    path = Path(publication.get_path_to_pdf())
    output_path = Path('data/thumbnails/' + str(publication.id) + '.png')
    
    # If the PDF file exists and the thumbnail does NOT exist, then create the thumbnail
    if path.is_file() and not output_path.is_file():
        print(f'{publication.id} - Creating thumbnail for publication "{publication.title}"')
        try:
            page = convert_from_path(path, 200, first_page=1, last_page=1)

            thumbnail_path = f'data/thumbnails/{publication.id}.png'
            try:
                page[0].save(thumbnail_path, 'PNG')
            except:
                print(f'Could not save thumbnail to path: {thumbnail_path}')

        except:
            print(f'Could not extract first page of PDF file.')


    # create_vikus_textures_and_sprites_for_publication(publication)

def create_vikus_textures_and_sprites_for_publication(publication):
    create_vikus_viewer_textures_and_sprites(str(publication.id))

def create_all_vikus_textures_and_sprites():
    create_vikus_textures_and_sprites("*")
    
def create_vikus_textures_and_sprites(files):
    
    directory_path = VIKUS_VIEWER_DATA_IMAGES_PATH

    # Create images folder if it does NOT exist
    Path(directory_path).mkdir(parents=True, exist_ok=True)

    sprite_path = f'{directory_path}{publication.id}.png'
    if not Path(sprite_path).is_file():
        os.system(f"vikus-viewer-script 'data/thumbnails/{files}.png' --output '{directory_path}' --spriteSize 90")

download_from_single_volume_years()

#print(get_last_valid_publication().get_path_to_pdf())

# read_data_csv()
# download()
# create_data_csv(publications)
# pdf_to_thumbnail(publications)
# create_vikus_textures_and_sprites()

# get_keywords_from_csv()
#for publication in publications.values():
#    # print(publication.id)
#    fulltext = publication.fulltext()
#    publication.set_keywords(fulltext)
# create_data_csv(publications)
