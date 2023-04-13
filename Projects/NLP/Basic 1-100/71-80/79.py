import nltk

raw = """DENNIS: Listen, strange women lying in ponds distributing swords 
is no basis for a system of government. Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
portertexts = [porter.stem(t) for t in tokens]
lancastertext = [lancaster.stem(t) for t in tokens]
print(portertexts)
print()
print(lancastertext)
