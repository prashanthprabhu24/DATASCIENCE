import nltk

entries = nltk.corpus.cmudict.entries()
words = [w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
print(words)
