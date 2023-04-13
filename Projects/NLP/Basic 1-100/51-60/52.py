from nltk.corpus import PlaintextCorpusReader

file = 'myCorpus.txt'
wordlists = PlaintextCorpusReader('', '.*')
print(wordlists.words(file))
