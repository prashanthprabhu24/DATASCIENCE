import nltk
from nltk.corpus import brown

suffix_fdist = nltk.FreqDist()

for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = list(dict(suffix_fdist).keys())[:100]
print(common_suffixes)
