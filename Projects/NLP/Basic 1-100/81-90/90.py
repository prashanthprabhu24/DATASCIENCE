import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents)*0.8)
train = brown_tagged_sents[:size]
test = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train, backoff=t0)
t2 = nltk.BigramTagger(train, backoff=t1)

accuracy = t2.accuracy(test)
print(accuracy*100)
