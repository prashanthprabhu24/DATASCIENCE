from nltk.corpus import brown

brown_news_tagged = brown.tagged_words(categories='news')
print(brown_news_tagged)
