import glob
import os
import numpy as np
import fitz
import datetime
from nltk import sent_tokenize
from nltk.corpus import stopwords
import nltk
from sentence_transformers import SentenceTransformer, util
import torch

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

    # maybe not a good idea, because "tracking-by-detection" --> "trackingbydetection"
    # maybe check if last char in an span is '-'?
    text = text.replace('-', ' ')
    return text

now = datetime.datetime.now()
nltk.download('punkt')
nltk.download('stopwords')

model = SentenceTransformer('all-mpnet-base-v2')

stops =set(stopwords.words('english'))

folder = r"C:\Users\GLJNI\Workspaces\EvoInt-Tracker-v.2\papers\2016-2021\10 aus 2021\*.pdf"

sent_embeddings_dict = {}
doc_embeddings_dict = {}

for file in glob.glob(rf'{folder}'):
    filepath = os.path.normpath(file)
    contents_raw = get_abstract_of_pdf(file)
    contents = contents_raw.lower()
    contents = contents.split()
    contents = [word for word in contents if word not in stops]
    contents = ' '.join(contents)
    print(contents)
    sentence_list = sent_tokenize(contents)
    sent_embeddings_dict.update({os.path.split(filepath)[1] : model.encode(sentence_list, convert_to_tensor=True, show_progress_bar=True)})


for file, value in sent_embeddings_dict.items():
    doc_embeddings_dict.update({file : torch.mean(sent_embeddings_dict[file],dim=0)})
    print("File: ", file, "Type: ", type(sent_embeddings_dict[file]), "Shape: ", sent_embeddings_dict[file].size())

final_tensor = torch.stack(list(doc_embeddings_dict.values()))

cosine_scores = util.cos_sim(final_tensor, final_tensor)

# print(final_tensor)
# print(type(final_tensor))
# print(final_tensor.size())
print(cosine_scores)


now2 = datetime.datetime.now()
time = now2-now
print(time)