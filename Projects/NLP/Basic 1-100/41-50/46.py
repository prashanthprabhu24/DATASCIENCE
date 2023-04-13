import nltk
from nltk.corpus import brown

news_text = brown.words(categories='news')
fdsit = nltk.FreqDist([w.lower() for w in news_text])

models = ['can', 'could', 'may', 'might', 'must', 'will']

for i in models:
    print(i + ':', fdsit[i])
