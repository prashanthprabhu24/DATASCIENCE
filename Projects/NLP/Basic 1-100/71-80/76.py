import feedparser
import nltk
from bs4 import BeautifulSoup

llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
post = llog.entries[2]
content = post.content[0].value

tokens = nltk.word_tokenize(BeautifulSoup(content, features='html.parser').get_text())
print(tokens[:20])
print(' '.join(tokens))