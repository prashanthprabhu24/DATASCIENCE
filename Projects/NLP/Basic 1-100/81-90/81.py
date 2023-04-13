import nltk

sents = "And now for something completely different"
text = nltk.word_tokenize(sents)
postag = nltk.pos_tag(text)
print(postag)
