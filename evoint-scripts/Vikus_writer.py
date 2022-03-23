#/usr/bin/python3

import os
import csv
import sys
from pathlib import Path

from Publication import publications, Publication
from DataRow import data_rows, get_data_row, create_from_row, DataRow

#
# data.csv
# --------
#
# 0  = global_id
# 1  = id
# 2  = year
# 3  = title
# 4  = authors
# 5  = abstract
# 6  = keywords
# 7  = pdf_link
# 8  = path_to_pdf
# 9 = fulltext
#

csv.field_size_limit(10000000)

csv_file = None
csv_file_reader = None

def get_data_csv_path():
    
    csv_path = '../vikus-viewer/data/data.csv'
    if not Path(csv_path).is_file():
        with open(csv_path,'w') as f:
            pass
    
    return csv_path

#Checking the file exists or not
def check_file_empty(path_of_file):
    #Checking if file exist and it is empty
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0

def order_by_id(dct):
    publications_list = [p for p in dct.values()]
    return sorted(list(publications_list), key=lambda x: int(x.id), reverse=False)

def clear_data_csv():
    with open(get_data_csv_path(), 'w') as f:
        pass

def open_csv_file_reader():
    
    global csv_file
    global csv_file_reader

    if csv_file == None:
        csv_file = open(get_data_csv_path(), 'r', encoding="utf-8")
        csv_file_reader = csv.reader(csv_file)     
        
        index = 0
        for row in csv_file_reader:
            
            if index > 0:
                create_from_row(row)
            index += 1    
            
    else:
        csv_file.seek(0, 0) # reset read and write position  

def close_csv_file_reader():
    global csv_file
    csv_file.close()
    
def get_csv_file_reader():
    global csv_file_reader
    open_csv_file_reader()
    return csv_file_reader

def get_data_rows():
    open_csv_file_reader()
    return data_rows

def get_publication_information_by_link(link):
    
    if len(get_data_rows()) == 0 or (len(publications) + 1) >= len(get_data_rows()):
        return None

    data_row = get_data_row(len(publications))
    
    if data_row.get_pdf_link() == link:
        return data_row
    else:
        print('NEED TO LOOK IN CSV-FILE', len(publications) + 1)
        for row in get_csv_file_reader():
            if row[6] == link:
                return get_data_row(row[2]) # row[2] -> id
    
    return None

def get_last_publication_link():
    
    # TODO: nicht https://www.ijcai.org/proceedings/2021/0001.pdf returnen, sondern None und dann im Downloader gucken ob ein Link existiert
    
    try:
        
        if len(get_data_rows()) == 0:
            return "https://www.ijcai.org/proceedings/2021/0001.pdf"
        
        return get_data_row(len(get_data_rows()) - 1).get_pdf_link()
    except Exception as e:
        print(f'Error while getting last publication information. {e}')
    
    return "https://www.ijcai.org/proceedings/2021/0001.pdf"

def get_last_valid_publication():
    
    if len(get_data_rows()) == 0:
        return None

    max_index = len(get_data_rows()) - 1

    for i in reversed(range(max_index + 1)):
        
        data_row = get_data_row(i)
        path_to_pdf = data_row.get_path_to_pdf()
        file_size = os.path.getsize(path_to_pdf)
        print(path_to_pdf, file_size)
        
        if file_size > 0:
            return data_row
        
    return None

def get_last_valid_publication_link():
    
    data_row = get_last_valid_publication()

    if data_row == None:
        return None
    else:
        return publication_entry.get_pdf_link()

def write_data_csv_header(csv_writer):
    
    if check_file_empty(get_data_csv_path()):
        csv_writer.writerow(['keywords'] +
                           ['year'] +
                           ['id'] +
                           ['_title'] +
                           ['_authors'] +
                           ['_abstract'] +
                           ['_origin_path'] +
                           ['_display_path_to_pdf'] +
                           ['_path_to_pdf'] +
                           ['_fulltext'])
        
def write_data_csv_row(csv_writer, publication):
    
    temp_a = publication.get_path_to_pdf().split('/')[-5:]
    display_path_to_pdf = '/'.join(temp_a)
    keywords = ','.join(publication.keywords) if len(publication.keywords) > 0 else 'None'
    
    data_row = get_data_row(publication.id)
    
    if data_row == None:
        data_row = DataRow(publication.id, publication.year, publication.title, publication.authors, 'None', keywords, publication.get_pdf_link(), display_path_to_pdf, publication.get_path_to_pdf())
    
    csv_writer.writerow(data_row.to_csv_row())

def add_to_data_csv(publication):
    
    with open(get_data_csv_path(), 'a+', newline='', encoding="utf-8") as csvfile:
        
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)

        write_data_csv_row(csv_writer, publication)

        # print(publication.id)

def create_data_csv(dct):
    with open(get_data_csv_path(), 'w', newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)
        
        for publication in order_by_id(dct):
            write_data_csv_row(csv_writer, publication)
            # print(publication.id)


# TODO: create_timeline_csv(dct_years):


def read_data_csv():
    exit('EEEEEEEEEEEERROR')
    with open(get_data_csv_path(), newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for line in csvreader:
            Publication(pub_id=line['id'],
                        title=line['_title'],
                        authors=line['_authors'],
                        year=line['year'],
                        origin_path=line['_origin_path'],
                        path_to_pdf=line['_path_to_pdf'])




def save_backup():
    create_data_csv(publications)


def restore_backup():
    read_data_csv()


def sample():
    Publication('0001', 'title', '1993', 'origin_path_oh', 'path to some pdf')
    Publication('0005', 't2itle', '12993', 'or2igin_path_oh', 'pa2th to some pdf')


#csv.field_size_limit(sys.maxsize)
# sample()
#
#
# save_backup()
# restore_backup()
