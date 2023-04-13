import nltk

names = nltk.corpus.names
print(names.fileids())
male_names = names.words('male.txt')
female_names = names.words('female.txt')
names = [w for w in male_names if w in female_names]
print(names)
