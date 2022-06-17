
from urllib.request import urlopen
from urllib.parse import urlparse
import os
from subprocess import DEVNULL, STDOUT, check_call
from pathlib import Path
from bs4 import BeautifulSoup
import fitz
from PIL import Image
import json
from datetime import datetime
import base64

from pdf2image import convert_from_path
from urllib.error import HTTPError

from Publication import publications, Publication
from VikusWriter import add_to_data_csv

#
# Every n downloads the progress will be printed.
# If None every single download the progress will be printed.
# 
PRINT_PROGRESS_STEP = 1000

IJCAI_URL = "https://www.ijcai.org/past_proceedings/"

VIKUS_VIEWER_PATH = "../vikus-viewer/"

VIKUS_VIEWER_DATA_PATH = VIKUS_VIEWER_PATH + "data/"
VIKUS_VIEWER_DATA_IMAGES_PATH = VIKUS_VIEWER_DATA_PATH + "images/"

VIKUS_VIEWER_DATA_FULLTEXT_PATH = VIKUS_VIEWER_DATA_PATH + "fulltext/"
VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH = VIKUS_VIEWER_DATA_FULLTEXT_PATH + "pdf/"

global_id = 0
debug = False

def get_year_folder_path(year):
    return f'{VIKUS_VIEWER_DATA_FULLTEXT_PDF_PATH}{year}/'

def string_encoding(s):
    string_bytes = base64.b64encode(s.encode('utf-8'))
    return str(string_bytes, 'utf-8')

def process_publication(title, authors, year, pdf_link):

    # base64-encoding to always have a suitable file name for the pdf file
    publication_id = string_encoding(pdf_link)
    
    if(debug):
        encoded_title = title.encode('utf8')
        print(f'[{year}] - [{publication_id}] Creating publication "{encoded_title}" with authors ({authors}) (from {pdf_link})')

    publication = create_publication_object(publication_id, title, authors, year, pdf_link)
    
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
            if debug:
                print(f'\t- Redownload of PDF required. Size of file is zero.')
        
    try:
        
        if(debug):
            print(f'\t- Downloading PDF file...')
            
        response = urlopen(publication.get_pdf_link())
        # TODO: path_to_pdf has to start at data/..., so add vikus-viewer/ here
        os.makedirs(get_year_folder_path(publication.year), exist_ok=True)
        file = open(publication.get_path_to_pdf(), 'wb')
        file.write(response.read())
        file.close()
        
    except HTTPError:
        print("Error writing file: " + publication.get_pdf_link())
    except TimeoutError:
        print("TimeoutError")


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
                if debug:
                    print(f'\t- Recreation of thumbnail required. Size of file is zero.')
        
        if(debug):
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

def create_vikus_textures_and_sprites(publication):
    
    directory_path = VIKUS_VIEWER_DATA_IMAGES_PATH

    Path(directory_path).mkdir(parents=True, exist_ok=True)

    sprite_path = f'{directory_path}{publication.id}.png'
    
    sprite_status = sprite_file_state(publication)
    if sprite_status > 0:
        
        if sprite_status == 2:
            if debug:
                print(f'\t- Recreation of sprite required. Size of file(s) is zero.') 
    
        if(debug):
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

def get_abstract_of_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    
    abstract_header_pdf_number = None
    abstract_text = ''
    
    for page_number in range(doc.page_count):
        
        page = doc.load_page(page_number)
        page_dict = page.get_text('dict')
        abstract_header_pdf_number = find_abstract_header_pdf_number(page_dict)
        #print(f'PDF Number: {abstract_header_pdf_number}')
        if abstract_header_pdf_number == None:
            continue
        
        abstract_text_node = page_dict['blocks'][abstract_header_pdf_number + 1] # +1, because next node
        abstract_text = concat_pdf_section_text(abstract_text_node)
        break
        
    if abstract_header_pdf_number == None:
        return None
        
    return abstract_text
    
    
def find_abstract_header_pdf_number(page_dict):
    for i in range(len(page_dict['blocks'])):
        
        node = page_dict['blocks'][i]
        
        if('lines' not in node or len(node['lines']) == 0):
            return None
        if('spans' not in node['lines'][0] or len(node['lines'][0]['spans']) == 0):
            return None
        if('text' not in node['lines'][0]['spans'][0]):
            return None
                
        if(node['lines'][0]['spans'][0]['text'].lower().strip() == 'abstract'):
            return int(node['number'])
    
        
def concat_pdf_section_text(node):
    text = ''
    
    for i in range(len(node['lines'])):
        for j in range(len(node['lines'][i]['spans'])):
            text += node['lines'][i]['spans'][j]['text'] + ' '
    
    text = text.replace('-', '') # maybe not a good idea, because "tracking-by-detection" --> "trackingbydetection"
    return text

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

def test_extract_abstracts():

    date = str(datetime.now())
    date = date.replace(' ', 'T').replace(':', '-')

    with open(f'./debug/extract_abstract_errors_{date}.txt', 'w') as file:
        file.write(file_path + '\n')
    
    for root, dirs, files in os.walk('D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/fulltext/pdf', topdown=True):
        dirs.sort(reverse=True)
        for name in files:
            file_path = os.path.join(root, name)
            file_path = file_path.replace('\\', '/')

            abstract_text = get_abstract_of_pdf(file_path)
            
            if abstract_text == None:
                with open(f'./debug/extract_abstract_errors_{date}.txt', 'a') as file:
                    file.write(file_path + '\n')
            
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

if __name__ == "__main__":
    test_extract_abstracts()
#get_abstract_of_pdf('D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/fulltext/pdf/2020/0795.pdf')

# not the full abstract
#print(get_abstract_of_pdf('D:/Studium/Semester4/Studienprojekt/EvoInt-Tracker-v.2/vikus-viewer/data/fulltext/pdf/1995/8486.pdf'))

#
# TODO:
# - remove_year_data(year) # in data.csv
# - remove_publication_data(id) # in data.csv 
#
#
#
