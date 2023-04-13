import nltk

entries = nltk.corpus.cmudict.entries()
words = [w for w, pron in entries if w[0].isalpha() and len(pron[0]) <= 2 and pron[0].lower() != w[0].lower() and len(pron) <= len(w)]
print(words)
for i in words:
    print(i, dict(entries)[i])
