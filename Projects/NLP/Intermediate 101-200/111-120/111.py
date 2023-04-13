import nltk

posts = nltk.corpus.nps_chat.xml_posts()[:10000]


def dialogue_act_feactures(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['Contains(%s)' % word.lower()] = True
    return features


featuresets = [(dialogue_act_feactures(post.text), post.get('class'))
               for post in posts]

size = int(len(featuresets) * 0.8)
train_set, test_set = featuresets[:size], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

accuracy = nltk.classify.accuracy(classifier, test_set)
print('Accuracy : ', accuracy*100)
