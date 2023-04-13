import nltk

entries = nltk.corpus.cmudict.entries()
print(dict(entries)['nicks'])
syllable = ['N', 'IH0', 'K', 'S']
# syllable = dict(entries)['nicks']
words = [w for w, pron in entries if pron[-4:] == syllable]
print(words)

