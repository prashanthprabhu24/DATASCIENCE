import nltk

sents = "They refuse to permit us to obtain the refuse permit"
text = nltk.word_tokenize(sents)
postag = nltk.pos_tag(text)
print(postag)
