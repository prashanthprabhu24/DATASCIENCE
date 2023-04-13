from nltk import book

print()
fdist1 = book.FreqDist(book.text1)
print(fdist1)
print(list(fdist1)[:10])  # Top 10
