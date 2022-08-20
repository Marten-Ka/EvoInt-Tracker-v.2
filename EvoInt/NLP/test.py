from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')

#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.']

#Sentences are encoded by calling model.encode()
sentence_embeddings = model.encode(sentences)

#Print the embeddings
print(len(sentence_embeddings[0]))