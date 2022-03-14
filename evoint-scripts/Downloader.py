from Publication import publications, Publication, get_keywords_from_csv
from collections import OrderedDict
from Vikus_writer import create_data_csv, read_data_csv, add_to_data_csv, clear_data_csv, get_last_publication_link, get_publication_information_by_link, close_csv_file_reader
from Year import years, Year
from urllib.request import urlopen
import urllib.parse
from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
from pathlib import Path

from time import time

from pdf2image import convert_from_path
from urllib.error import HTTPError
import sys


def parse_title(title):
    title = title.replace('\n', ' ')
    title = title.replace('\t', ' ')
    title = title.replace('  ', ' ')
    title = title.strip()
    return title


def next_pub_id():
    ids = [int(pub_id) for pub_id in publications.keys()]
    ids.sort()
    result = str(ids[-1] + 1) if len(ids) > 0 else '0'
    return result.zfill(4)

def download_publications(pubs=None):
    if pubs is None:
        pubs = publications
    total = len(pubs.values())
    for key, pub in pubs.items():
        # check if file is already downloaded
        if Path(pub.path_to_pdf).is_file():
            continue
        try:
            print(f'{str(round((float(key)/total) * 100, 2))}% ({key}/{total}) - Downloading Publication "{pub.title}" \n\tfrom {pub.origin_path}\n')
            response = urlopen(pub.origin_path)
            # TODO: path_to_pdf has to start at data/..., so add vikus-viewer/ here
            os.makedirs(pub.path_to_pdf[:-8], exist_ok=True)
            file = open(pub.path_to_pdf, 'wb')
            file.write(response.read())
            file.close()
        except HTTPError:
            print("error writing file: " + pub.origin_path)
            continue
        except TimeoutError:
            print("TimeoutError")
            continue
        
def download_publication(publication):
    
    if Path(publication.path_to_pdf).is_file():
        return
        
    try:
        print(f'Downloading Publication "{publication.title}" \n\t\tfrom {publication.origin_path}\n')
        response = urlopen(publication.origin_path)
        # TODO: path_to_pdf has to start at data/..., so add vikus-viewer/ here
        os.makedirs(publication.path_to_pdf[:-8], exist_ok=True)
        file = open(publication.path_to_pdf, 'wb')
        file.write(response.read())
        file.close()
    except HTTPError:
        print("error writing file: " + publication.origin_path)
    except TimeoutError:
        print("TimeoutError")

def is_link_to_volume(link: str):
    year = link.split("/")[-1]
    if not year:
        year = link.split("/")[-2]
    # print(year)
    return year[:4].isdigit()

# URLs, wo man Daten downloaden kann
def get_available_volumes(index_page_url=None):
    result = set()
    if index_page_url is None:
        index_page_url = "https://www.ijcai.org/past_proceedings/"
    response = urlopen(index_page_url)
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find('div', 'content')
    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link.split("/")[-1] == "2017":
            current_link = current_link + "/"
        if is_link_to_volume(current_link):
            # if index_page_url not in current_link:
            #     current_link = urllib.parse.urljoin(index_page_url, current_link)
            if current_link not in result:
                result.add(current_link)
    return sorted(result, reverse=True)

def download_from_single_volume_years():
    
    if not Path("../vikus-viewer/data/data.csv").is_file():
        with open("../vikus-viewer/data/data.csv", "w") as f:
            pass

    # clear_data_csv()
    
    # last available data from publication
    last_publication_link = get_last_publication_link()
    last_publication_reached = False
    
    pdf_count_0722 = 0

    base_pdf_path = '../vikus-viewer/data/fulltext/pdf/'
    base_url = "https://www.ijcai.org/past_proceedings/"

    available_volumes = get_available_volumes(base_url)
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
        for link in soup.find_all('a'):
            current_link = link.get('href')
            
            if volume_link not in current_link:
                current_link = urllib.parse.urljoin(volume_link, current_link)
            if current_link.endswith('.pdf') and current_link not in visited_links:
                visited_links.append(urllib.parse.urljoin(volume_link, current_link))

                if not urlparse(current_link).scheme:
                    current_link = 'https://' + current_link
                    
                pub_id = next_pub_id()
                title = parse_title(link.text)
                if title == "here" or current_link == f'https://www.ijcai.org/proceedings/{year}/preface.pdf':
                    return

                authors = ""

                # TODO: Following lines in own Method. Check if link is actually a publication.
                if title == "PDF":  # TODO: missing for years 2015, 2016
                    if int(year) >= 2017:
                        paper_wrapper = link.find_parent("div", "paper_wrapper")
                        title = paper_wrapper.find("div", "title")
                        title = parse_title(title.text)
                        authors = paper_wrapper.find("div", "authors").text
                
                if title == "Self-Adaptive Swarm System (SASS)":
                    pdf_count_0722 += 1
                    if pdf_count_0722 == 1:
                        continue
                    
                #
                # If the last publication, which is in the data.csv, was already reached, then we can only
                # download the next publications.
                # Because of that, we don't need to download publications, we already downloaded.
                #
                if last_publication_reached:
                    create_new_publication(current_link, base_pdf_path, year, pub_id, title, authors)
                else:
                    
                    #
                    # We try to create a publication from the data in the data.csv.
                    # If it fails, because the data row was not found, we create the
                    # publication with the link.
                    #
                    
                    success = create_available_publication(current_link, year)
                    
                    if not success:
                        create_new_publication(current_link, base_pdf_path, year, pub_id, title, authors)
                
                if get_last_publication_link == current_link:
                    last_publication_reached = True
                    close_csv_file_reader()

    #create_data_csv(publications)

#
# Tries to create a publication object from data.csv-entry
# Returns if data was available
#
def create_available_publication(current_link, year):
    
    publication_information = get_publication_information_by_link(current_link)
    
    if publication_information == None:
        print(f'Tried to create publication with link "{current_link}" (from data.csv), but no information was available.')
        return False
    else:
        
        pub_id = publication_information[2]
        title = publication_information[3]
        #if(int(pub_id) % 50 == 0):
        #    print(f'{year}: [{pub_id}] Creating publication "{title}" (from data.csv)')
        print(f'{year}: [{pub_id}] Creating publication "{title}" (from data.csv) [{current_link}]')
        Publication(pub_id=pub_id,
                    title=title,
                    authors=publication_information[4],
                    year=publication_information[1],
                    origin_path=publication_information[6],
                    path_to_pdf=publication_information[8])
        return True

#
# Creates a publication object from a link
#
def create_new_publication(current_link, base_pdf_path, year, pub_id, title, authors):

    path_to_pdf = base_pdf_path + str(year) + '/' + str(pub_id) + '.pdf'
    encoded_title = title.encode('utf8')
    #if(int(pub_id) % 50 == 0):
    #    print(f'{year}: [{pub_id}] Creating publication "{encoded_title}" (from {current_link})')
    print(f'{year}: [{pub_id}] Creating publication "{encoded_title}" (from {current_link})')
    publication = Publication(pub_id=pub_id,
                                title=title,
                                authors=authors,
                                year=year,
                                origin_path=current_link,
                                path_to_pdf=path_to_pdf)
    
    #to_download = OrderedDict()
    #to_download[0] = publication
    #download(to_download)
    
    download_publication(publication)

    add_to_data_csv(publication)
    pdf_to_thumbnail(publication)

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

    path = Path(publication.path_to_pdf)
    output_path = Path('data/thumbnails/' + str(publication.id) + '.png')
    # If the PDF file exists and the thumbnail does NOT exist, then create the thumbnail
    if path.is_file() and not output_path.is_file():
        print(f'{publication.id} - Creating Thumbnail for Publication "{publication.title}"')
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

    directory_path = '../vikus-viewer/data/images'

    # Create images folder if it does NOT exist
    Path(directory_path).mkdir(parents=True, exist_ok=True)

    sprite_path = f'../vikus-viewer/data/images/{publication.id}.png'
    if not Path(sprite_path).is_file():
        os.system(f"vikus-viewer-script 'data/thumbnails/{publication.id}.png' --output '../vikus-viewer/data/images' --spriteSize 90")

def create_vikus_textures_and_sprites():
    # for pub in publications.values():
    #     os.system(f'node ../vikus-viewer-script/bin/textures "data/thumbnails/{pub.id}.png" --output "../vikus-viewer/data/images"')
    # os.system("ulimit -n 16100; node ../vikus-viewer-script/bin/textures 'data/thumbnails/*.png' --output '../vikus-viewer/data/images'")
    os.system("vikus-viewer-script 'data/thumbnails/*.png' --output '../vikus-viewer/data/images' --spriteSize 90")


download_from_single_volume_years()

# read_data_csv()
# download()
# create_data_csv(publications)
# pdf_to_thumbnail(publications)
# create_vikus_textures_and_sprites()

# get_keywords_from_csv()
for publication in publications.values():
    # print(publication.id)
    fulltext = publication.fulltext()
    publication.set_keywords(fulltext)
# create_data_csv(publications)
