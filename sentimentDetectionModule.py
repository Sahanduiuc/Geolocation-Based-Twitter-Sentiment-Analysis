# Sentiment Analysis Module
# Classifies the Sentiment and its Confidence
# Uses 7 classifiers and makes final decision based on max votes
# Trained Classifiers provided in TrainedClassifiers Folder

# If you want to train the Module, uncomment the code and train it.

# import os
import nltk
import random
# from nltk.classify.scikitlearn import SklearnClassifier
import pickle

# from sklearn.naive_bayes import MultinomialNB, BernoulliNB
# from sklearn.linear_model import LogisticRegression, SGDClassifier
# from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode

from nltk.tokenize import word_tokenize


# Tweet Classification using Votes from all Classifiers
class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    # Classify Tweets based on Positive or Negative Sentiment
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    # Calculate Confidence of Classification
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

# Input Data
# short_pos = open("Train_Test_Data/positive.txt", "r").read()
# short_neg = open("Train_Test_Data/negative.txt", "r").read()

# Create Directory to save Trained Classifiers to reduce Training Time
# directory = 'TrainedClassifiers'
# if not os.path.exists(directory):
#     os.makedirs(directory)

# all_words = []
# documents = []


# J is adjective, r is adverb, v is verb
# allowed word types = ['J','R','V']

# allowed_word_types = ['J']
#
# for r in short_pos.split('\n'):
#     documents.append((r, "pos"))
#     words = word_tokenize(r)
#     pos = nltk.pos_tag(words)
#     for w in pos:
#         if w[1][0] in allowed_word_types:
#             all_words.append(w[0].lower())
#
# for r in short_neg.split('\n'):
#     documents.append((r, "neg"))
#     words = word_tokenize(r)
#     pos = nltk.pos_tag(words)
#     for w in pos:
#         if w[1][0] in allowed_word_types:
#             all_words.append(w[0].lower())
#
# save_documents = open('TrainedClassifiers/documents.pickle','wb')
# pickle.dump(documents, save_documents)
# save_documents.close()

documents_f = open('TrainedClassifiers/documents.pickle','rb')
documents = pickle.load(documents_f)
documents_f.close()

# all_words = nltk.FreqDist(all_words)
#
# word_features = list(all_words.keys())[:5000]
#
# save_word_features = open('TrainedClassifiers/word_features.pickle','wb')
# pickle.dump(word_features, save_word_features)
# save_word_features.close()

word_features_f = open('TrainedClassifiers/word_features.pickle','rb')
word_features = pickle.load(word_features_f)
word_features_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# featuresets = [(find_features(rev), category) for (rev, category) in documents]
#
# save_featuresets = open('TrainedClassifiers/featuresets.pickle','wb')
# pickle.dump(featuresets, save_featuresets)
# save_featuresets.close()

featuresets_f = open('TrainedClassifiers/featuresets.pickle', 'rb')
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))

# positive data example:
training_set = featuresets[:10000]
testing_set = featuresets[10000:]


# -------------------------- Naive Bayes Classifier ----------------------
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
# classifier.show_most_informative_features(15)
# save_classifier = open('TrainedClassifiers/OriginalNaiveBayes.pickle','wb')
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/OriginalNaiveBayes.pickle','rb')
classifier = pickle.load(open_file)
open_file.close()


# ---------------------------- MNB Classifier ----------------------
# MNB_Classifier = SklearnClassifier(MultinomialNB())
# MNB_Classifier.train(training_set)
# print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/MNBclassifier.pickle', 'wb')
# pickle.dump(MNB_Classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/MNBclassifier.pickle','rb')
MNB_classifier = pickle.load(open_file)
open_file.close()



# ------------------------ BernoulliNB Classifier ------------------------
# BernoulliNB_Classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_Classifier.train(training_set)
# print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/BernoulliNB.pickle', 'wb')
# pickle.dump(BernoulliNB_Classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/BernoulliNB.pickle','rb')
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()


# ----------------------- Logistic Regression Classifier ---------------------------
# LogisticRegression_Classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_Classifier.train(training_set)
# print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/LogisticRegression.pickle', 'wb')
# pickle.dump(LogisticRegression_Classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/LogisticRegression.pickle','rb')
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()



# ---------------------------- SGD Classifier ---------------------------
# SGD_Classifier = SklearnClassifier(SGDClassifier())
# SGD_Classifier.train(training_set)
# print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGD_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/SGDClassifier.pickle', 'wb')
# pickle.dump(SGD_Classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/SGDClassifier.pickle','rb')
SGD_classifier = pickle.load(open_file)
open_file.close()



# -------------------------------- Linear SVC Classifier ---------------------------
# LinearSVC_Classifier = SklearnClassifier(LinearSVC())
# LinearSVC_Classifier.train(training_set)
# print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/LinearSVC.pickle', 'wb')
# pickle.dump(LinearSVC_Classifier, save_classifier)
# save_classifier.close()

open_file = open('TrainedClassifiers/LinearSVC.pickle','rb')
LinearSVC_classifier = pickle.load(open_file)
open_file.close()



# ------------------------------ NuSVC Classifier ------------------------------
# NuSVC_Classifier = SklearnClassifier(NuSVC())
# NuSVC_Classifier.train(training_set)
# print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_Classifier, testing_set)) * 100)
# save_classifier = open('TrainedClassifiers/NuSVC.pickle', 'wb')
# pickle.dump(NuSVC_Classifier, save_classifier)
# save_classifier.close()
#
open_file = open('TrainedClassifiers/NuSVC.pickle','rb')
NuSVC_classifier = pickle.load(open_file)
open_file.close()



voted_classifier = VoteClassifier(classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  SGD_classifier,
                                  LinearSVC_classifier,
                                  NuSVC_classifier)

# print("Voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

# ---------------------------------- EOC ---------------------------------
