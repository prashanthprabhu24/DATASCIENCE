import nltk
from nltk.corpus import brown

brown_news_tagged = brown.tagged_words(categories='news')

tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd = sorted(zip(tag_fd.values(), tag_fd.keys()), reverse=True)
print(list(dict(tag_fd).values()))

