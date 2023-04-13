from nltk import book

print()
fdist1 = book.FreqDist(book.text1)
print(fdist1)
print(dict(fdist1))
