import nltk
from nltk.corpus import brown

days = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
categories = ['news', 'romance']

cfd = nltk.ConditionalFreqDist(
    (category, word)
    for category in categories
    for word in brown.words(categories=category)
)

tab = cfd.tabulate(conditions=categories, samples=days)
print(tab)

cfd.plot()
