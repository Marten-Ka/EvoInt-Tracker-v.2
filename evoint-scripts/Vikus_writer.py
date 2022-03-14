from Publication import publications, Publication
import csv
import sys

csv.field_size_limit(10000000)

csv_file = None
csv_file_reader = None
csv_content_list = []

import os

#Checking the file exists or not
def check_file_empty(path_of_file):
    #Checking if file exist and it is empty
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0

def order_by_id(dct):
    publications_list = [p for p in dct.values()]
    return sorted(list(publications_list), key=lambda x: int(x.id), reverse=False)

def clear_data_csv():
    with open("../vikus-viewer/data/data.csv",'w') as f:
        pass

def open_csv_file_reader():
    
    global csv_file
    global csv_file_reader
    global csv_content_list
    
    if csv_file == None:
        csv_file = open('../vikus-viewer/data/data.csv', 'r', encoding="utf-8")
        csv_file_reader = csv.reader(csv_file)
        csv_content_list = list(get_csv_file_reader())
    else:
        csv_file.seek(0, 0) # reset read and write position  

def close_csv_file_reader():
    global csv_file
    csv_file.close()
    
def get_csv_file_reader():
    global csv_file_reader
    open_csv_file_reader()
    return csv_file_reader

def get_csv_content_list():
    global csv_content_list
    
    open_csv_file_reader()
    return csv_content_list

def get_publication_information_by_link(link):
    
    if len(get_csv_content_list()) == 0 or (len(publications) + 1) >= len(get_csv_content_list()):
        return None

    entry = get_csv_content_list()[len(publications) + 1]
    
    if entry[6] == link:
        return entry
    else:
        print('NEED TO LOOK IN CSV-FILE')
        for row in get_csv_file_reader():
            if row[6] == link:
                return row
    
    return None

def get_last_publication_link():
    
    # TODO: nicht https://www.ijcai.org/proceedings/2021/0001.pdf returnen, sondern None und dann im Downloader gucken ob ein Link existiert
    
    try:
        
        if len(get_csv_content_list()) == 0:
            return "https://www.ijcai.org/proceedings/2021/0001.pdf"
        
        return get_csv_content_list()[len(get_csv_content_list()) - 1][6] 
    except Exception as e:
        print(f'Error while getting last publication information. {e}')
    
    return "https://www.ijcai.org/proceedings/2021/0001.pdf"

def add_to_data_csv(publication):
    with open('../vikus-viewer/data/data.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if check_file_empty('../vikus-viewer/data/data.csv'):
            csvwriter.writerow(['keywords'] +
                               ['year'] +
                               ['id'] +
                               ['_title'] +
                               ['_authors'] +
                               ['_abstract'] +
                               ['_origin_path'] +
                               ['_display_path_to_pdf'] +
                               ['_path_to_pdf'] +
                               ['_fulltext'])

        temp_a = publication.path_to_pdf.split('/')[-5:]
        display_path_to_pdf = '/'.join(temp_a)
        keywords = ','.join(publication.keywords) if len(publication.keywords) > 0 else 'None'
        csvwriter.writerow([f'{keywords}'] +
                            [publication.year] +
                            [publication.id] +
                            [publication.title] +
                            [publication.authors] +
                            ['abstract comes here'] +
                            [publication.origin_path] +
                            [display_path_to_pdf] +
                            [publication.path_to_pdf] + [f'{publication.fulltext()}'])
        # print(publication.id)

def create_data_csv(dct):
    with open('../vikus-viewer/data/data.csv', 'w', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['keywords'] +
                           ['year'] +
                           ['id'] +
                           ['_title'] +
                           ['_authors'] +
                           ['_abstract'] +
                           ['_origin_path'] +
                           ['_display_path_to_pdf'] +
                           ['_path_to_pdf'] +
                           ['_fulltext'])
        for publication in order_by_id(dct):
            temp_a = publication.path_to_pdf.split('/')[-5:]
            display_path_to_pdf = '/'.join(temp_a)
            keywords = ','.join(publication.keywords) if len(publication.keywords) > 0 else 'None'
            csvwriter.writerow([f'{keywords}'] +
                               [publication.year] +
                               [publication.id] +
                               [publication.title] +
                               [publication.authors] +
                               ['abstract comes here'] +
                               [publication.origin_path] +
                               [display_path_to_pdf] +
                               [publication.path_to_pdf] + [f'{publication.fulltext()}'])
            # print(publication.id)


# TODO: create_timeline_csv(dct_years):


def read_data_csv():
    with open('../vikus-viewer/data/data.csv', newline='') as csvfile:
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
