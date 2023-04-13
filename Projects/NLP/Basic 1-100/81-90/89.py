from nltk.corpus import brown
import nltk

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.80)
train, test = brown_tagged_sents[:size], brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train, cutoff=1, backoff=t0)
t2 = nltk.BigramTagger(train, cutoff=1, backoff=t1)
t3 = nltk.TrigramTagger(train, cutoff=1, backoff=t2)
t4 = nltk.NgramTagger(4, train, cutoff=1, backoff=t3)

accuracy = t4.accuracy(test)
print(accuracy * 100)
