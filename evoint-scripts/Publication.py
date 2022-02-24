import csv
from collections import OrderedDict
import fitz
import re
from collections import Counter

publications = OrderedDict()
KEYWORDS = [
    'perceive',
    'acquire',
    'recognize',
    'learn',
    'adapt',
    'solve',
    'achieve',
    'understand',
    'find',
    'maintain',
    'improve',
    'evolve',
    'think',
    'explain',
    'generate',
    'reason',
    'plan',
    'predict',
    'act',
    'exhibit',
    'behave',
    'change',
    'perform',
    'pursue',
    'communicate',
    'interact',
    'execute',
    'respond',
    'machine',
    'ability',
    'human',
    'environment',
    'goal',
    'system',
    'knowledge',
    'problem',
    'information',
    'experience',
    'human',
    'cognitive',
    'general',
    'artificial',
    'high',
    'physical',
    'complex',
    'computational',
    'social',
    'real world',
    'natural world',
    'physical world',
    'human intelligence',
    'artificial intelligence',
    'general intelligence'
]


class Publication:
    def __init__(self, pub_id, title, year, origin_path, path_to_pdf, authors=None):
        self.id = pub_id
        self.title = title
        self.authors = authors
        self.keywords = []
        self.year = year
        self.origin_path = origin_path
        self.path_to_pdf = path_to_pdf

        self.add_to_publications()

    def add_to_publications(self):
        publications[self.id] = self

    def fulltext(self, path=None):
        if path is None:
            path = self.path_to_pdf
        result = ""
        try:
            doc = fitz.open(path)
            for page in doc:
                result += page.getText(flags=0) + " "
            result = self.filter_symbols(result)
        except:
            print(f'{self.id} - no fulltext')

        result = result.replace('International Joint Conference on Artificial Intelligence', ' ')
        # keyword 'artificial intelligence' would be in every publication. so the title of the conference needs to be removed
        return result.lower()

    def filter_symbols(self, text):
        return re.sub(r'[.!?*+&%",;:\'`´’‘”“()\[\]{}]', ' ', text)

    def get_word_count(self, text):
        return Counter([w for w in text.split() if len(w) > 1]).most_common()

    def set_keywords(self, fulltext):
        for keyword in KEYWORDS:
            if keyword in fulltext:
                self.keywords.append(keyword)


def get_publication_by_title(title):
    for pub in publications.values():
        if pub.title == title:
            return pub
        else:
            print(f'"{title}" not found')


def get_keywords_from_csv():
    with open('data/csv/IJCAI_1997-2017_purified_lower.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for line in csvreader:
            csv_title = line['Paper'].replace('\n', ' ')
            csv_title = csv_title.replace('\t', ' ')
            csv_title = csv_title.replace('  ', ' ')
            csv_title = csv_title.strip()
            print(csv_title)
            pub = get_publication_by_title(csv_title)
            if pub:
                print(f'{pub.title} - {csv_title}')

# def save_backup():
#
#     with open('publications_backup.json', 'w') as fp:
#         for publication in publications.values():
#             json.dump(publication.__dict__, fp)
#             fp.write("\n")


# def restore_backup():
#     with open('publications_backup.json', 'r') as fp:
#         lines = fp.read().splitlines()
#         for line in lines:
#             temp = json.loads(line)
#
#             Publication(pub_id=temp['id'],
#                         title=temp['title'],
#                         year=temp['year'],
#                         origin_path=temp['origin_path'],
#                         path_to_pdf=temp['path_to_pdf'])


def sample():
    Publication('0001', 'title', '1993', 'origin_path_oh', 'path to some pdf')
    Publication('0005', 't2itle', '12993', 'or2igin_path_oh', 'pa2th to some pdf')


# sample()
# save_backup()
# restore_backup()
get_keywords_from_csv()
