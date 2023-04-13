from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()

raw = BeautifulSoup(html, features="html.parser").get_text()  # nltk.clean_html(html), deprecated
# print(raw)
tokens = nltk.word_tokenize(raw)
# print(tokens)
text = nltk.Text(tokens[96:399])
print(text)
print(text.concordance('gene'))
