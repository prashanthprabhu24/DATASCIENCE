from nltk import book

print()
fdist1 = book.FreqDist(book.text1)
print(fdist1['whale'], book.text1.count('whale'))
