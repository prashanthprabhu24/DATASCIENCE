from nltk import book

print()
V = set(book.text4)
long_words = [w for w in V if len(w) > 15]
print(long_words)