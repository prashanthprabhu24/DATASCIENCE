from nltk.corpus import brown
import nltk

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents)*0.80)
train, test = brown_tagged_sents[:size], brown_tagged_sents[size:]

unigram_tagger = nltk.UnigramTagger(train)

accuracy = unigram_tagger.accuracy(test)
print(accuracy*100)
