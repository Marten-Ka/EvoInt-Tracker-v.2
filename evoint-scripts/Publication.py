import csv
from collections import OrderedDict
import fitz
import re
from collections import Counter
from pathlib import Path

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
    def __init__(self, publication_id, title, year, origin_path, path_to_pdf, authors=None):
        self.id = publication_id
        self.title = title
        self.authors = authors
        self.keywords = []
        self.year = year
        self.origin_path = origin_path
        self.path_to_pdf = path_to_pdf

        self.add_to_publications()

    def add_to_publications(self):
        publications[self.id] = self

    def get_pdf_link(self):
        return self.origin_path

    def get_path_to_pdf(self):
        return self.path_to_pdf

    def get_display_path_to_pdf(self):
        temp_a = self.get_path_to_pdf().split('/')[-5:]
        return '/'.join(temp_a)

    def get_keywords(self, fulltext):
        if len(self.keywords) == 0:
            keywords = []
            for keyword in KEYWORDS:
                if keyword in fulltext:
                    keywords.append(keyword)
            self.keywords = ','.join(keywords)
        return self.keywords

    def get_encoded_title(self):
        return self.title.encode('utf8')

    def fulltext(self):
        result = ""
        try:
            doc = fitz.open(self.get_path_to_pdf())
            for page in doc:
                result += page.get_text(flags=0) + " "
            result = self.filter_symbols(result)
        except Exception as e:
            print(f'{self.id} - no fulltext')

        result = result.replace(
            'International Joint Conference on Artificial Intelligence', ' ')
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

    def to_csv_row(self):
        fulltext = self.fulltext()
        return ([f'{self.get_keywords(fulltext)}'] +
                [self.year] +
                [self.id] +
                [self.title] +
                [self.authors] +
                [get_abstract_of_pdf(self.get_path_to_pdf())] +
                [self.origin_path] +
                [f'{self.get_display_path_to_pdf()}'] +
                [self.path_to_pdf] +
                [f'{fulltext}'])


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

        # +1, because next node
        abstract_text_node = page_dict['blocks'][abstract_header_pdf_number + 1]
        abstract_text = concat_pdf_section_text(abstract_text_node)
        break

    if abstract_header_pdf_number == None:
        return None

    return abstract_text


def concat_pdf_section_text(node):
    text = ''

    for i in range(len(node['lines'])):
        for j in range(len(node['lines'][i]['spans'])):
            text += node['lines'][i]['spans'][j]['text'] + ' '

    # maybe not a good idea, because "tracking-by-detection" --> "trackingbydetection"
    # maybe check if last char in an span is '-'?
    text = text.replace('-', '')
    return text


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
                pass
                print(f'{pub.title} - {csv_title}')
