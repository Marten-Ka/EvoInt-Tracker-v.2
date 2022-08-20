import datetime
import glob
import os
from collections import defaultdict
from tkinter import N

import fitz
import nltk
import torch
import pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler
from nltk import pos_tag, sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer, util

def get_abstract_of_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    abstract_header_pdf_number = None
    abstract_text = ''

    for page_number in range(doc.page_count):

        page = doc.load_page(page_number)
        page_dict = page.get_text('dict')
        abstract_header_pdf_number = find_abstract_header_pdf_number(page_dict)
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

    # '-' as line seperator causes '- ' in text -> replace it an keep '-' as word seperator
    text = text.replace('- ', '')
    return text

now = datetime.datetime.now()
nltk.download('punkt', 'stopwords','omw-1.4', 'averaged_perceptron_tagger')

model = SentenceTransformer('all-mpnet-base-v2')

stops =set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

#tag map for part-of-speech-tagging and lemmatization
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

folder = input("Enter a path to a folder containing papers\nEnter the path without quotation marks\n")
folder += "\*.pdf"

sent_embeddings_dict = {}
doc_embeddings_dict = {}

for file in glob.glob(rf'{folder}'):
    filepath = os.path.normpath(file)
    contents_raw = get_abstract_of_pdf(file)
    contents = contents_raw.lower()
    contents = contents.split()
    contents = [word for word in contents if word not in stops]
    contents = [lemmatizer.lemmatize(word, tag_map[tag[0]]) for word, tag in pos_tag(contents)]
    contents = ' '.join(contents)
    sentence_list = sent_tokenize(contents)
    print(sentence_list)
    sent_embeddings_dict.update({os.path.split(filepath)[1] : model.encode(sentence_list, convert_to_tensor=True, show_progress_bar=True)})

for file, value in sent_embeddings_dict.items():
    doc_embeddings_dict.update({file : torch.mean(sent_embeddings_dict[file],dim=0)})
    #print("File: ", file, "Type: ", type(sent_embeddings_dict[file]), "Shape: ", sent_embeddings_dict[file].size())

final_tensor = torch.stack(list(doc_embeddings_dict.values()))

x = StandardScaler().fit_transform(final_tensor)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(x)
principal_df = pandas.DataFrame(data=principal_components, columns= ['x', 'y'])

principal_df.to_csv("tsne(NLP).csv", sep=",")
# principal_df.plot(x='x', y='y', style='o')
# for k, v in principal_df.iterrows():
#     plt.annotate(k, v)

# plt.show()

# cosine_scores = util.cos_sim(final_tensor, final_tensor)

# i = 1
# for item in cosine_scores:
#     print(i, item)
#     i = i + 1


now2 = datetime.datetime.now()
time = now2-now
print(time)
