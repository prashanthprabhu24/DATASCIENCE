from nltk import book

print()
fdist1 = book.FreqDist(book.text1)
fdist1.plot(50, cumulative=True, percents=True)
