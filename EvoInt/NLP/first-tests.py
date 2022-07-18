import glob
import os
import nltk
import fitz
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer
from torch import embedding

nltk.download('punkt')

model = SentenceTransformer('all-mpnet-base-v2')

folder = r"C:\Users\MDKaf\Workspaces\EvoInt-Tracker-v.2\some-papers\*.pdf"

sentences_dict = {}

for file in glob.glob(rf'{folder}'):
    filepath = os.path.normpath(file)
    #print(file_path)
    contents = ""
    with fitz.open(r"C:\Users\MDKaf\Workspaces\EvoInt-Tracker-v.2\some-papers\ABAMAS_Distance Polymatrix Coordination Games 2021.pdf") as doc:
        for page in doc:
            contents += page.get_text()
    contents = contents.replace("\n", " ")
    sentence_list = sent_tokenize(contents)
    #sentences_dict = {os.path.split(filepath)[1] : sentence_list}
    embedding1 = model.encode(sentence_list, convert_to_tensor=True)
#print("---", filepath, "---")
#print(contents)
print(embedding1)