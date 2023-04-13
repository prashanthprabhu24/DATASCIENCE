from urllib.request import urlopen
import nltk

url = "https://www.gutenberg.org/files/2554/2554-0.txt"
raw = str(urlopen(url).read())

tokens = nltk.word_tokenize(raw)
print(len(raw), len(tokens))
print(tokens[:10])
