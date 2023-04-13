from nltk import book

print()
print('How many times on average each word is used : ', len(book.text3)/len(set(book.text3)))
