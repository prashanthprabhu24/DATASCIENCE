import nltk
from nltk.corpus import brown

suffix_fdist = nltk.FreqDist()

for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = list(dict(suffix_fdist).keys())[:100]


def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features


tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
size = int(len(featuresets) * 0.1)
train, test = featuresets[size:], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train)

accuracy = nltk.classify.accuracy(classifier, test)
print('Accuracy : ', accuracy)
