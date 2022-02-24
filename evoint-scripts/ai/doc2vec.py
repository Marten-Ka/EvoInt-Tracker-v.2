# Manage the Imports
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import csv
import re
import nltk

nltk.download('punkt')
from nltk import stem
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import fitz
import os

MAX_PUBLICATIONS = 10  # total 10632


def load_data(path_to_dir, year=0):
    count = 0

    # clear data files
    with open(f'{year}_data.csv', mode='w', newline='') as f:
        f.write('')
    with open('articleIds.txt', mode='w', newline='') as f:
        f.write('')

    result_articles = []
    result_ids = []
    p = re.compile(r'\d{4}$')
    for dirpath, dirnames, filenames in os.walk(path_to_dir):
        if re.search(p, dirpath):
            y = dirpath[-4:]
            if y == str(year) or str(0) == str(year):
                for filename in [f for f in filenames if f.endswith('.pdf')]:
                    text = ""
                    try:
                        doc = fitz.open(dirpath + '/' + filename)
                        for page in doc:
                            text += page.getText(flags=0) + " "
                        text = filter_symbols(text)
                    except:
                        print(f'no fulltext for: {filename}')

                    text = text.replace('International Joint Conference on Artificial Intelligence', ' ')
                    text = text.replace('-\n', '')
                    text = text.replace('\n', ' ')
                    result_articles.append(text.lower())
                    result_ids.append(filename[:-4])

                    with open(f'{year}_data.csv', 'a', newline='') as csvfile:
                        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvwriter.writerow([text.lower()])
                    with open('articleIds.txt', mode='a', newline='') as f:
                        f.write(filename[:-4] + '\n')

                    if count % 10 == 0:
                        percent = (count / MAX_PUBLICATIONS) * 100
                        print("load data: " + str(round(percent, 1)) + " %")
                    count += 1

                    if len(result_articles) >= MAX_PUBLICATIONS:
                        break
                else:
                    continue
                break
        else:
            continue
        break
    return result_articles, result_ids


# def create_id_list(path, year):
#     p = re.compile(r'\d{4}$')
#     with open('articleIds.txt', mode='w', newline='') as f:
#         for dirpath, dirnames, filenames in os.walk(path):
#             if re.search(p, dirpath):
#                 y = dirpath[-4:]
#                 if y == str(year) or y == str(0):
#                     for filename in [f for f in filenames if f.endswith('.pdf')]:
#                         f.write(filename[:-4] + '\n')


def filter_symbols(text):
    return re.sub(r'[.!?*+&%",;:\'`´’‘”“()\[\]{}]', ' ', text)


# Remove stop word tokens by using NLTKs English stop word library
def removeStopwords(stringset):
    stop_words = set(stopwords.words("english"))
    filtered_set = []
    for word in stringset:
        if word.lower() not in stop_words:
            filtered_set.append(word)
    return filtered_set


def splitByRegEx(reviews):
    unfiltered_tokens = []
    regex_statement = '[a-zA-Záéíóú]+'
    tokenizer = tokenize.RegexpTokenizer(regex_statement)

    for review in reviews:
        unfiltered_tokens.append(tokenizer.tokenize(review))
    print("Split by RegEx")
    return unfiltered_tokens


# Remove stop word tokens
def removeStopWordsToken(unfilteredTokens):
    filtered_tokens = []
    for review in unfilteredTokens:
        filtered_tokens.append(removeStopwords(review))
    print("Stopwords removed")
    return filtered_tokens


# Stem the remaining words
def stemming(filteredTokens):
    stemmed_tokens = []
    stemmer = stem.snowball.EnglishStemmer()
    for review in filteredTokens:
        stemmed_tokens_temp = []
        for token in review:
            stemmed_tokens_temp.append(stemmer.stem(token))
        stemmed_tokens.append(stemmed_tokens_temp)
    print("Stemming was successful")
    return stemmed_tokens


# Merge common multi word expressions into one token
def mergeCommonAbbr(stemmedTokens):
    merged_tokens = []
    dictionary = [
        ('e', 'g')
    ]
    tokenizer = tokenize.MWETokenizer(dictionary, separator='_')
    for review in stemmedTokens:
        merged_tokens.append(tokenizer.tokenize(review))
    print("Merged the common Word Expressions")
    return merged_tokens


#Count the total Number of Tokens
def countTokens(allTokens):
    token_count = 0
    for review in allTokens:
        if len(review)>0:
            for token in review:
                token_count+=1
    print("Number of all tokens: ", token_count)


#Create List of all tokens and IDs
def createTokenList(merged_tokens, reviews_ids):
    for i in range(0, len(merged_tokens)):
        merged_tokens[i].insert(0, reviews_ids[i])
    print("Token List is created")
    #print(merged_tokens)
    return merged_tokens


# Save preprocessed data to .csv file, using ',' as delimiter between 2 tokens and quoting each token with '
def saveSentences(merged_tokens):
    with open('preprocessedReviews.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar="\'", quoting=csv.QUOTE_ALL)
        for definition in merged_tokens:
            csv_writer.writerow(definition)

    print("Wrote dataset to ", csv_file.name)


#recreate the sentences with the preprocessed words and give it an ID
def recreateSentence(merged_tokens=None):
    stemmed_sentences = []
    id = []
    i = 1
    for review in merged_tokens:
        tmp = ""
        review.pop(0)
        for word in review:
            tmp += str(word)+" "
            id.append(i)
            i += 1
        stemmed_sentences.append(tmp)

    #give every document an id
    tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(stemmed_sentences)]
    return tagged_data, stemmed_sentences


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
    max_epochs = 100
    vec_size = 2
    alpha = 0.025

    model = Doc2Vec(vector_size=vec_size,
                    alpha=alpha,
                    min_alpha=0.00025,
                    min_count=20,
                    dm=method)

    print("Build vocab:")
    import time
    start = time.time()
    model.build_vocab(tagged_data)
    end = time.time()
    t = (end - start) / 60
    print("Vocab created! It took " + str(round(t, 2)) + " minutes.")
    print()


    start = time.time()

    print("Start Training:")
    for epoch in range(max_epochs):
        if epoch % 1 == 0:
            percent = (epoch / max_epochs) * 100
            c = time.time()
            print("Training (epoch " + str(epoch) + ") - " + str(round(percent, 1)) + "% (" + str(round(((c - start) / 60), 2)) + " minutes)")
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    end = time.time()
    t = (end - start) / 60
    print("Vectors are created. It took " + str(round(t, 2)) + " minutes.")
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


def create_fake_tsne(path, id_tmp=None):
    tsne_tmp = []
    # id_tmp = []
    with open(path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for line in csvreader:
            tsne_tmp.append((line['x_vector'], line['y_vector']))

    # with open('./articleIds.txt') as idfile:
    #     id_tmp = idfile.read().splitlines()

    filename = "tsne.csv"
    with open(filename, 'w') as tsne_file:
        tsne_file.write("id,x,y")
        tsne_file.write('\n')
        for article_id, coord in zip(id_tmp, tsne_tmp):
            line = f'{article_id},{coord[0]},{coord[1]}'
            tsne_file.write(line)
            tsne_file.write('\n')


def main():
    # main
    # articles, ids = load_data("../data/backup/fulltext")
    # print(len(articles))
    # print(len(ids))
    # create_id_list("../data/backup/fulltext", 2013)
    # unfiltered_tokens = splitByRegEx(articles)
    # filtered_tokens = removeStopWordsToken(unfiltered_tokens)
    # stemmed_tokens = stemming(filtered_tokens)
    # merged_tokens = mergeCommonAbbr(stemmed_tokens)
    # countTokens(merged_tokens)
    # merged_tokens = createTokenList(merged_tokens, reviews_ids)
    # saveSentences(merged_tokens)
    # tagged_data, stemmed_sentences = recreateSentence(merged_tokens)
    # trainDoc2Vec(tagged_data, stemmed_sentences, 0)  # 0 for distributed Bag of Words, 1 for distributed Memory
    # trainDoc2Vec(tagged_data, stemmed_sentences, 1)
    # create_fake_tsne("./doc2vec_dbow_2d.csv", ids)

    tagged_data, stemmed_sentences = recreateSentenceFromFile('preprocessedReviews.csv')
    trainDoc2Vec(tagged_data, stemmed_sentences, 0)  # 0 for distributed Bag of Words, 1 for distributed Memory
    # create_fake_tsne("./doc2vec_dbow_2d.csv")

if __name__ == '__main__':
    main()
