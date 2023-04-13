from nltk import book

print()
text = ['more', 'is', 'said', 'than', 'done']
print(list(book.bigrams(text)))
# print(list(book.bigrams(book.text4)))
# print(list(book.bigrams(book.text8)))
