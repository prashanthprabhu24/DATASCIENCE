from nltk import book

print()
print('Number of Times "lol" appears in text5 : ', book.text5.count('lol'))
print('Average usage of all words in text5 : ', len(book.text5)/len(set(book.text5)))
print('Percentage of the text is taken up by word "lol" in text5 : ',  100 * book.text5.count('lol')/len(book.text5))
