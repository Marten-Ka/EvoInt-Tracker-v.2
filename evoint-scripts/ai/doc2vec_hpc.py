# Manage the Imports
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import csv
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

MAX_PUBLICATIONS = 10  # total 10632


def recreateSentenceFromFile(filename):
    merged_tokens = []
    with open(filename, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar="\'", quoting=csv.QUOTE_ALL)
        for definition in csv_reader:
            merged_tokens.append(definition)

    stemmed_sentences = []
    id = []
    i = 1
    print(len(merged_tokens))
    for iteration, review in enumerate(merged_tokens):
        if iteration % 100 == 0:
            percent = (iteration / len(merged_tokens)) * 100
            print("recreate sentence from file - " + str(round(percent, 1)) + "%")
        tmp = ""
        # review.pop(0)
        for word in review:
            tmp += str(word)+" "
            id.append(i)
            i += 1
        stemmed_sentences.append(tmp)

    #give every document an id
    tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(stemmed_sentences)]
    return tagged_data, stemmed_sentences


# Create Doc2Vec Model and train it
def trainDoc2Vec(tagged_data, stemmed_sentences, method):
    # train the doc2vec model
    max_epochs = 250
    vec_size = 2
    alpha = 0.025

    model = Doc2Vec(vector_size=vec_size,
                    alpha=alpha,
                    min_alpha=0.00025,
                    min_count=5,
                    dm=method)

    print("Build vocab:")
    model.build_vocab(tagged_data)
    print("Vocab created!")

    import time
    start = time.time()

    print("Start Training:")
    for epoch in range(max_epochs):
        if epoch % 1 == 0:
            percent = (epoch / max_epochs) * 100
            print("Training (epoch " + str(epoch) + ") - " + str(round(percent, 1)) + "%")
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    end = time.time()
    time = (end - start) / 60
    print("Vectors are created. It took " + str(time) + " minutes.")
    print()

    modelname = "test_doc2vecDBOW.model" if method == 0 else "test_doc2vecDM.model"
    model.save(modelname)
    print("Model Saved to " + modelname)

    # get the vectors out of the model, connect it with the definition names and safe the data
    vectors = []
    for i in range(len(stemmed_sentences)):
        vector = model.dv[str(i)]
        vec_tmp = str(i) + "," + str(vector[0]) + "," + str(vector[1])
        vectors.append(vec_tmp)

    filename = "test_doc2vec_dbow_2d.csv" if method == 0 else "test_doc2vec_dm_2d.csv"
    with open(filename, 'w') as file:
        file.write("review_id,x_vector,y_vector")
        file.write('\n')
        for vector in vectors:
            file.write(vector)
            file.write('\n')


def main():
    tagged_data, stemmed_sentences = recreateSentenceFromFile('preprocessedReviews.csv')
    trainDoc2Vec(tagged_data, stemmed_sentences, 0)  # 0 for distributed Bag of Words, 1 for distributed Memory


if __name__ == '__main__':
    main()
