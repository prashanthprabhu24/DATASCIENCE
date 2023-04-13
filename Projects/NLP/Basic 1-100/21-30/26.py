from nltk import book

print()


def lexical_diversity(text):
    return len(text)/len(set(text))


def percentage(count, total):
    return 100 * count / total


print(lexical_diversity(book.text3))
print(lexical_diversity(book.text5))
print(percentage(book.text4.count('a'), len(book.text4)))
