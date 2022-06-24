# /usr/bin/python3

import os
import csv
from pathlib import Path

from Publication import publications, Publication
from DataRow import data_rows, get_data_row, create_from_row, DataRow
import Downloader

csv.field_size_limit(10000000)

csv_file = None
csv_file_reader = None


def get_data_csv_path():

    csv_path = '../vikus-viewer/data/data.csv'
    if not Path(csv_path).is_file():
        with open(csv_path, 'w') as f:
            pass

    return csv_path

# Checking the file exists or not


def check_file_empty(path_of_file):
    # Checking if file exist and it is empty
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0


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
        csv_file.seek(0, 0)  # reset read and write position


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

    encoded_link = Downloader.encode_string(link)
    data_row = get_data_row(encoded_link)

    if data_row.get_pdf_link() == link:
        return data_row
    else:
        print('NEED TO LOOK IN CSV-FILE', len(publications) + 1)
        for row in get_csv_file_reader():
            if row[6] == link:
                return get_data_row(row[2])  # row[2] -> id

    return None


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
    keywords = ','.join(publication.keywords) if len(
        publication.keywords) > 0 else 'None'

    data_row = get_data_row(publication.id)

    if data_row == None:
        data_row = DataRow(publication.id, publication.year, publication.title, publication.authors, 'None',
                           keywords, publication.get_pdf_link(), display_path_to_pdf, publication.get_path_to_pdf())

    csv_writer.writerow(data_row.to_csv_row())


def add_to_data_csv(publication):

    with open(get_data_csv_path(), 'a+', newline='', encoding="utf-8") as csvfile:

        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)

        write_data_csv_row(csv_writer, publication)

        # print(publication.id)


def create_data_csv():
    with open(get_data_csv_path(), 'w', newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_data_csv_header(csv_writer)

        for publication in list(publications):
            write_data_csv_row(csv_writer, publication)


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


def restore_backup():
    read_data_csv()

# csv.field_size_limit(sys.maxsize)
# sample()
#
#
# save_backup()
# restore_backup()
