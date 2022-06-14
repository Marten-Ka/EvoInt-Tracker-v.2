
import sys
from collections import OrderedDict
from urllib.request import urlopen
import urllib.parse
from urllib.parse import urlparse
import os
from subprocess import DEVNULL, STDOUT, check_call
from pathlib import Path
from bs4 import BeautifulSoup
from time import time
import fitz
from PIL import Image

from pdf2image import convert_from_path
from urllib.error import HTTPError

from Publication import publications, Publication, get_keywords_from_csv
from Vikus_writer import create_data_csv, read_data_csv, add_to_data_csv, clear_data_csv, get_last_publication_link, get_last_valid_publication, get_last_valid_publication_link, get_publication_information_by_link, close_csv_file_reader

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

def clean_text(string):
    string = string.replace('\n', ' ').replace('\t', ' ').replace('  ', ' ').replace('&nbsp;', '').replace('&nbsp', '').replace(u'\ufffd', '').replace(u'\xa0', '').replace(u'\xe2', '').replace(u'\x80', '').replace(u'\x94', '').strip()
    
    # replace multiple whitespaces
    while '  ' in string:
        string = string.replace('  ', ' ')
        
    while ',,' in string:
        string = string.replace(',,', ',')
        
    while ';;' in string:
        string = string.replace(';;', ';')
        
    while string[-1] == ';':
        string = string[0:-1]
        
    return string
        
# searches for the next available id
def next_pub_id():
    ids = [int(pub_id) for pub_id in publications.keys()]
    ids.sort()
    result = str(ids[-1] + 1) if len(ids) > 0 else '0'
    return result.zfill(4)

def get_id_from_link(link): # https://www.ijcai.org/proceedings/2020/0085.pdf
    id = link.split('/')    
    id = id[len(id) - 1]    # 0085.pdf
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
        else:
            print(f'\t- Redownload of PDF required. Size of file is zero.')
        
    try:
        
        if(PRINT_PROGRESS_STEP == None or (int(data_row.id) % PRINT_PROGRESS_STEP == 0)):
            print(f'\t- Downloading PDF file...')
            
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
        
        #
        # Ignore the year 2001, because the site
        # does not provide any information?
        # Visit: https://www.ijcai.org/proceedings/2001-1
        #   and: https://www.ijcai.org/proceedings/2001-2
        #
        if current_link.split("/")[-1] == "2001-1" or current_link.split("/")[-1] == "2001-2":
            continue
        if is_link_to_volume(current_link):
            if current_link not in result:
                result.add(current_link)
    
    return ['https://www.ijcai.org/proceedings/1993-2', 'https://www.ijcai.org/proceedings/1993-1']            
    # return sorted(result, reverse=True)

def download_from_single_volume_years():
    
    if not Path(VIKUS_VIEWER_DATA_PATH + "data.csv").is_file():
        with open(VIKUS_VIEWER_DATA_PATH + "data.csv", "w") as f: # create file
            pass

    # last available data from publication
    last_publication_link = get_last_publication_link()
    last_publication_reached = False
    
    pdf_count_0722 = 0

    base_pdf_path = VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH

    available_volumes = get_available_volumes()
    print('Parsing the following websites: ' + ', '.join(available_volumes))

    for volume_link in available_volumes:
        
        # example for volume_link: https://www.ijcai.org/proceedings/2021/
        year = volume_link.split("/")[-1][:4] # example: 2021
        if not year:
            year = volume_link.split("/")[-2][:4]
        os.makedirs(base_pdf_path + year, exist_ok=True)

        visited_links = []
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
                
                #
                # This listed publication contains an
                # a-Tag with the wrong link to the PDF.
                #
                if current_link == 'https://www.ijcai.org/proceedings/Papers/IJCAI07-107.pdf':
                    current_link = 'https://www.ijcai.org/Proceedings/09/Papers/107.pdf'
                
                publication_id = next_pub_id()
                
                title = clean_text(link.text)
                if title == "here" or current_link == f'https://www.ijcai.org/proceedings/{year}/preface.pdf':
                    continue

                valid_publication, title, authors = get_pdf_information(int(year), link, title)
                
                if valid_publication:
                
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

def get_pdf_information(year, link_tag, origin_title):
    
    try:       
        
        paper_wrapper = None
        title = None
        authors = ''   
        
        if year >= 2015:
            
            if origin_title != 'PDF':
                return False, origin_title, []
            
        else:
            
            if origin_title == "Abstract":
                return False, origin_title, []
        
        if year >= 2017:
            paper_wrapper = link_tag.find_parent("div", "paper_wrapper")
        else:
            paper_wrapper = link_tag.find_parent("p")
        
        
        if year >= 2017:
            
            title = paper_wrapper.find("div", "title")
            title = clean_text(title.text)
            authors = paper_wrapper.find("div", "authors").text
            
        elif year == 2016 or year == 2015:
            
            title = paper_wrapper.text.split("\n")[0] # example: Preface / xxxiii
            title = title.rsplit(' / ', 1)[0] # example: Preface
            title = clean_text(title)
            
            author_container = None
            
            if year == 2016:
                author_container = paper_wrapper.find("i")
            elif year == 2015:
                author_container = paper_wrapper.find("em")
            
            authors = author_container.text
        
        elif year == 2013 or year == 2011 or year == 2009 or year == 2007:

            #
            # Some headlines contain a-Tags.
            # We need to ignore those.
            #
            if paper_wrapper == None:
                return False, origin_title, []
            
            a_tags = paper_wrapper.find_all('a')            
            
            if len(a_tags) >= 2:
                
                abstract_a_tag = None
                title_a_tag = None
                
                if year == 2013 or year == 2011:
                    abstract_a_tag = a_tags[1]
                    title_a_tag = a_tags[0]
                elif year == 2009 or year == 2007:                   
                    abstract_a_tag = a_tags[0]
                    title_a_tag = a_tags[1]
                
                #
                # If the wrapper has a link to an abstract
                # we assume it is a publication.
                # 
                if "Abstract" in abstract_a_tag.text:
                    
                    title = clean_text(title_a_tag.text)
                    authors = paper_wrapper.find("i").text
                    
        elif year == 2005:
            
            title = clean_text(link_tag.text)
            
            title_wrapper = link_tag.find_parent('p', class_='doctitle')
            author_wrapper = title_wrapper.find_next_sibling()
            authors = author_wrapper.text
        
        elif year == 2003:
            
            title = clean_text(link_tag.text)
            
            title_wrapper = link_tag.find_parent('p')
            author_wrapper = title_wrapper.find_next_sibling()
            
            if author_wrapper == None:
                return False, title, []
            authors = author_wrapper.text

        elif year == 1999 or year == 1997 or year == 1995:
            
            #
            # The year 1999 has two seperate sites:
            # https://www.ijcai.org/proceedings/1999-1 and
            # https://www.ijcai.org/proceedings/1999-2
            #
            # They both are not exactly structured the same.
            # The first site has a b-Tag around the text, whereas
            # the second site not.
            # Therefore we need to make a few checks.
            #
            
            #print("----------------")

            title = clean_text(link_tag.text)
            
            link_parent = link_tag.find_parent('b')
            title_wrapper = None
            
            if link_parent == None:
                title_wrapper = link_tag.find_parent('p')
            else:
                
                #
                # Some publications have a b-Tag as a
                # "grandparent". We need to check if one
                # child has a a-Tag.
                #
                
                if len(link_parent.contents) >= 1:
                    title_wrapper = link_tag.find_parent('p')
                else:
                    title_wrapper = link_parent.find_parent('p')
                
            #print(link_tag.text)
            #print(title_wrapper)
            
            author_wrapper = title_wrapper.find_next_sibling()
            
            if author_wrapper == None:
                return False, title, []
            
            b_author_tag = author_wrapper.find('b')
            
            #print(b_author_tag)
            #print(author_wrapper)
            
            if b_author_tag == None:
                authors = author_wrapper.text
            else:
                authors = b_author_tag.text
            
            #
            # The text inside the author wrapper
            # contains a digits and dots at the end.
            #
            authors = remove_dots_and_numbers_at_end(authors)
        
        elif year == 1993:
            
            title = clean_text(link_tag.text)
            
            #
            # This author tag is an a-Tag.
            # Therefore the program thinks it is a publication.
            #
            if(title == 'Henri Be ringer and Bruno de Backer.'):
                return False, title, []
            
            #
            # Authors sometimes are seperated into two or more p-Tags
            # Example for a structure:
            #
            #   <p>
            #       <a href="...">TITLE</a>
            #   </p>
            #
            #   <p>AUTHOR1, AUTHOR2</p>
            #   <p>and AUTHOR3..52</p>
            #
            # We use the ".." plus a number (we don't know what the number is for)
            # to identify if it is still a p-Tag with author information
            # or whether it is the next section.
            #
            
            current_tag = link_tag.find_parent('p')
            
            #
            # This publication has a different layout:
            #
            # <p>
            #   <a href="https://www.ijcai.org/Proceedings/93-1/Papers/024.pdf">Situation Recognition: Representation and Algorithms</a>
            #   Christophe Dousson, Paul Gaborit and Malik Ghallab..166
            # </p>
            #
            if(title == 'Situation Recognition: Representation and Algorithms'):
                
                authors = clean_text(current_tag.text.replace('Situation Recognition: Representation and Algorithms', ''))
                authors = remove_dots_and_numbers_at_end(authors)
                
            else:
            
                raw_authors = ''
                while(len(raw_authors) == 0 or not string_ends_with_dots_or_numbers(raw_authors)):
                
                    author_wrapper = current_tag.find_next_sibling()
                    current_tag = author_wrapper
                    
                    author_text = clean_text(author_wrapper.text)
                    raw_authors += author_text
                    authors += remove_dots_and_numbers_at_end(author_text) + ' '
            
        else:
            raise f'Year {year} not implemented!'
            
        valid_publication = True
        
        if title == None or authors == None:
            valid_publication = False
        
        return valid_publication, title, normalize_authors_string(authors)

    except Exception as e:
        print(f'Error while retrieving information: {e}')
        exit(0)
        return False, title, authors

def authors_string_to_array(authors):
    authors = clean_text(authors)
    
    #
    # We can't just replace the word 'and' with a comma,
    # because then names like 'Alexander' would be
    # changed to 'Alex,er'. We need to check if the
    # and is inside a name.
    #
    
    words = authors.split(' ')
    new_words = []
    
    for i in range(len(words)):
        
        if(words[i] == 'and' or words[i] == ',and' or words[i] == 'and,'):
            continue
        
        if((i + 1) < len(words) and words[i + 1].lower() == 'and'):
            word = words[i] + ',' if(words[i][-1] != ',') else words[i]
            new_words.append(word)
        else:
            new_words.append(words[i])
    
    return new_words

def normalize_authors_string(authors):
    return ' '.join(authors_string_to_array(authors))

def remove_dots_and_numbers_at_end(text):
    
    while(text[-1].isdigit() or text[-1] == '.' or text[-1] == ' '):
        text = text[0:-1]
    
    return text

def string_ends_with_dots_or_numbers(text):
    text = text.strip()
    return text[-1].isdigit() or text[-1] == '.';

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
        
        # publication = create_available_publication(current_link, year)
        
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
        download_publication(publication) # need to redownload, if the file size is 0
        publication_to_thumbnail(publication)
        create_vikus_textures_and_sprites(publication)
                
        return publication

#
# Creates a publication object from a link
#
def create_new_publication(publication_id, title, authors, year, current_link):

    encoded_title = title.encode('utf8')
    if(PRINT_PROGRESS_STEP == None or (int(global_id) % PRINT_PROGRESS_STEP == 0)):
        print(f'[{year}] - [{publication_id}] Creating publication "{encoded_title}" with authors ({authors}) (from {current_link})')

    publication = create_publication_object(publication_id, title, authors, year, current_link)
    
    download_publication(publication)

    add_to_data_csv(publication)
    publication_to_thumbnail(publication)
    create_vikus_textures_and_sprites(publication)
    
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
def publications_to_thumbnail(dct):
    for publication in dct.values():
        publication_to_thumbnail(publication)

# TODO: actually use var output_path on save
# Create thumbnail for one publications
def publication_to_thumbnail(publication):

    directory_path = 'data/thumbnails'

    # Create thumbnail folder if it does NOT exist
    Path(directory_path).mkdir(parents=True, exist_ok=True)

    path = Path(publication.get_path_to_pdf())
    output_path = Path('data/thumbnails/' + str(publication.id) + '.png')
    
    # If the PDF file exists and the thumbnail does NOT exist, then create the thumbnail
    if path.is_file():
        
        if output_path.is_file():
            file_size = os.path.getsize(output_path)
            
            if file_size > 0:
                return
            else:
                print(f'\t- Recreation of thumbnail required. Size of file is zero.')
        
        if(PRINT_PROGRESS_STEP == None or (int(publication.id) % PRINT_PROGRESS_STEP == 0)):
            print(f'\t- Creating thumbnail...')
            
        try:
            page = convert_from_path(path, 200, first_page=1, last_page=1)

            thumbnail_path = f'data/thumbnails/{publication.id}.png'
            try:
                page[0].save(thumbnail_path, 'PNG')
            except:
                print(f'\t- Could not save thumbnail to path: {thumbnail_path}')

        except:
            print(f'\t- Could not extract first page of PDF file.')

#def create_vikus_textures_and_sprites_for_publication(publication):
#    create_vikus_textures_and_sprites(str(publication.id))

#def create_all_vikus_textures_and_sprites():
#    create_vikus_textures_and_sprites("*")
    
def create_vikus_textures_and_sprites(publication):
    
    directory_path = VIKUS_VIEWER_DATA_IMAGES_PATH

    # Create images folder if it does NOT exist
    Path(directory_path).mkdir(parents=True, exist_ok=True)

    sprite_path = f'{directory_path}{publication.id}.png'
    
    sprite_status = sprite_file_state(publication)
    if sprite_status > 0:
        
        if sprite_status == 2:
            print(f'\t- Recreation of sprite required. Size of file(s) is zero.') 
    
        if(PRINT_PROGRESS_STEP == None or (int(publication.id) % PRINT_PROGRESS_STEP == 0)):
            print(f'\t- Creating sprite...')
            
        # stdout=DEVNULL hides the output of the script
        check_call(["node", "../vikus-viewer-script/bin/textures", f'data/thumbnails/{publication.id}.png', "--output", "../vikus-viewer/data/images", "--spriteSize", "90"], stdout=DEVNULL, stderr=STDOUT)

#
# Returns the state of the sprite files.
# 0 - downloaded
# 1 - not downloaded
# 2 - file exists, but is empty
#
def sprite_file_state(publication):
    
    return_code = 0
    
    base_directory_path = VIKUS_VIEWER_DATA_IMAGES_PATH
    file_path_90 = f'{base_directory_path}tmp/90/{publication.id}.png'
    file_path_1024 = f'{base_directory_path}1024/{publication.id}.jpg'
    file_path_4096 = f'{base_directory_path}4096/{publication.id}.jpg'

    paths = [ file_path_90, file_path_1024, file_path_4096 ]
    
    for path in paths:
        
        if Path(path).is_file():
            
            file_size = os.path.getsize(path)
        
            if file_size == 0:
                os.remove(path)
                return_code = max(return_code, 2)
                
        else:
            return_code = max(return_code, 1)          
        
    return return_code
            
# download_from_single_volume_years()

def get_abstract_of_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    page_dict = page.get_text('dict')
    abstract_header_pdf_number = find_abstract_header_pdf_number(page_dict)
    #print(abstract_header_pdf_number)
    abstract_text_node = page_dict['blocks'][abstract_header_pdf_number + 1] # +1, because next node
    abstract_text = concat_pdf_section_text(abstract_text_node)
    #print(abstract_text)
    return abstract_text
    
    
def find_abstract_header_pdf_number(page_dict):
    for i in range(len(page_dict['blocks'])):
        node = page_dict['blocks'][i]
        if(node['lines'][0]['spans'][0]['text'].lower().strip() == 'abstract'):
            return int(node['number'])
    
        
def concat_pdf_section_text(node):
    text = ''
    
    for i in range(len(node['lines'])):
        for j in range(len(node['lines'][i]['spans'])):
            text += node['lines'][i]['spans'][j]['text']
    
    text = text.replace('-', '') # maybe not a good idea, because "tracking-by-detection" --> "trackingbydetection"
    return text

#
# Error:
# File: D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/fulltext/pdf\2020\0795.pdf
#------------ ABSTRACT -----------------
#
#Traceback (most recent call last):
#  File "D:\Studium\Semester4\Studienprojekt\EvoInt-Tracker-v.2\evoint-scripts\Downloader.py", line 722, in <module>
#    abstract_test()
#  File "D:\Studium\Semester4\Studienprojekt\EvoInt-Tracker-v.2\evoint-scripts\Downloader.py", line 704, in abstract_test
#    print(get_abstract_of_pdf(file_path))
#  File "D:\Studium\Semester4\Studienprojekt\EvoInt-Tracker-v.2\evoint-scripts\Downloader.py", line 673, in get_abstract_of_pdf
#    abstract_text_node = page_dict['blocks'][abstract_header_pdf_number + 1] # +1, because next node
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#
#
#
def abstract_test():
    
    for root, dirs, files in os.walk('D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/fulltext/pdf', topdown=True):
        dirs.sort(reverse=True)
        for name in files:
            file_path = os.path.join(root, name)
            print(f'File: {file_path}')
            print(f'------------ ABSTRACT -----------------\n')
            print(get_abstract_of_pdf(file_path))
            
            if False:
                doc = fitz.open(file_path)
                page = doc.load_page(0)
                pix = page.get_pixmap()
                
                img = Image.open(f'D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/images/4096/{name.split(".")[0]}.jpg')
                img.show()
                
                print('\nIs the abstract correct? Type "y" for yes and "n" for no. Anything else with close the program')
                answer = input('').lower()
                
                if answer != 'y':
                    exit()
                    
                img.close()
            
abstract_test()

#
# TODO:
# - remove_year_data(year) # in data.csv
# - remove_publication_data(id) # in data.csv 
#
#
#
