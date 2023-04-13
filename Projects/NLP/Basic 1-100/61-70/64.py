import nltk

entries = nltk.corpus.cmudict.entries()
print(len(entries), entries)

for entry in entries:
    print(entry)
