from nltk.corpus import gutenberg

print(gutenberg.fileids())

for fileid in gutenberg.fileids():  # For every files.
    num_chars = len(gutenberg.raw(fileid))  # Number of Characters.
    num_words = len(gutenberg.words(fileid))  # Number of Words.
    num_sents = len(gutenberg.sents(fileid))  # Number of Sentences.
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))  # Number of Vocabulary
    print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)
