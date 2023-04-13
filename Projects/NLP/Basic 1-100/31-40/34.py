from nltk import book

print()
fdist = book.FreqDist(book.text5)
token = [w for w in set(book.text5) if len(w) > 7 and fdist[w] > 7]
print(token)

