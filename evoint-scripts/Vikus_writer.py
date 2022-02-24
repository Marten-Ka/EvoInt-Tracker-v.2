from Publication import publications, Publication
import csv
import sys


def order_by_id(dct):
    publications_list = [p for p in dct.values()]
    return sorted(list(publications_list), key=lambda x: int(x.id), reverse=False)


def create_data_csv(dct):
    with open('../vikus-viewer/data/data.csv', 'w', newline='') as csvfile:
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
            print(publication.id)


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
