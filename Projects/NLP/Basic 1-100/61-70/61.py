import nltk

puzzle_letters = nltk.FreqDist('egivronl')
obligatory = 'r'
worldlist = nltk.corpus.words.words()
sol = [w for w in worldlist if len(w) >= 4 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]
print(len(sol), sol)
