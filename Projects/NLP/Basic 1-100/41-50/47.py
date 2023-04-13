import nltk
from nltk.corpus import brown

govt_text = brown.words(categories='government')
fdist = dict(nltk.FreqDist([w.lower() for w in govt_text]))

models = 'wh'

for k in fdist.keys():
    if k.startswith(models):
        print(k, ':', fdist[k])
