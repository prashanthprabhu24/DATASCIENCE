import nltk
from nltk.corpus import names
import random

def gender_features(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastleter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features



names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n, g) in names]
size = 0.80
train, test = featuresets[:int(size * len(featuresets))], featuresets[int(size * len(featuresets)):]

classifier = nltk.NaiveBayesClassifier.train(train)

print(classifier.classify(gender_features('Neo')))
print(classifier.classify(gender_features('Trinity')))

accuracy = nltk.classify.accuracy(classifier, test)
print('Accuracy : ', accuracy * 100)
