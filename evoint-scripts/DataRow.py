import csv
from collections import OrderedDict
import fitz
import re
import os
from collections import Counter

data_rows = OrderedDict()

def get_data_row(id):
    if id in data_rows:
        return data_rows[id]
    else:
        return None

def create_from_row(row):
    return DataRow(row[2], row[1], row[3], row[4], row[5], row[0], row[6], row[7], row[8])

class DataRow:
    def __init__(self, publication_id, year, title, authors, abstract, keywords, origin_path, display_path_to_pdf, path_to_pdf):
        self.id = publication_id
        self.year = year
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.keywords = keywords
        self.origin_path = origin_path
        self.display_path_to_pdf = display_path_to_pdf
        self.path_to_pdf = path_to_pdf
        
        self.add_to_rows()

    def add_to_rows(self):
        data_rows[self.id] = self
        
    def get_pdf_link(self):
        return self.origin_path
    
    def get_path_to_pdf(self):
        return self.path_to_pdf

    def get_encoded_title(self):
        return self.title.encode('utf8')

    def fulltext(self, path=None):
        if path is None:
            path = self.get_path_to_pdf()
        result = ""
        try:
            doc = fitz.open(path)
            for page in doc:
                result += page.get_text(flags=0) + " "
            result = self.filter_symbols(result)
        except:
            print(f'{self.id} - no fulltext')

        result = result.replace('International Joint Conference on Artificial Intelligence', ' ')
        # keyword 'artificial intelligence' would be in every publication. so the title of the conference needs to be removed
        return result.lower()
    
    def filter_symbols(self, text):
        return re.sub(r'[.!?*+&%",;:\'`´’‘”“()\[\]{}]', ' ', text)

    def to_csv_row(self):
        return ([f'{self.keywords}'] +
                [self.year] +
                [self.id] +
                [self.title] +
                [self.authors] +
                [self.abstract] +
                [self.origin_path] +
                [self.display_path_to_pdf] +
                [self.path_to_pdf] +
                [f'{self.fulltext()}'])