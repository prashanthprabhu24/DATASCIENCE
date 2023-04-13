import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://pl.wikipedia.org/wiki/Depozyt_berli%C5%84ski"
raw = str(urlopen(url).read())
text = BeautifulSoup(raw, features="html.parser").get_text()
text = nltk.word_tokenize(text)
print(text)
