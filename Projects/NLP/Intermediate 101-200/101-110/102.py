from nltk.corpus import names
import random, nltk


def gender_feature(word):
    return {'feature': ''.join([word[0], word[-1]])}


names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_feature(n), g) for (n, g) in names]
size = 0.80
train, test = featuresets[:int(size * len(featuresets))], featuresets[int(size * len(featuresets)):]

classifier = nltk.NaiveBayesClassifier.train(train)
# print(classifier.classify(gender_feature('Neo')))
# print(classifier.classify(gender_feature('Trinity')))

accuracy = nltk.classify.accuracy(classifier, test)
print('Accuracy : ', accuracy * 100)
