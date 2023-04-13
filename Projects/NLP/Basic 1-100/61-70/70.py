from nltk.corpus import swadesh

lans = swadesh.fileids()
print(lans)

for i in [139, 140, 141, 142]:
    print(swadesh.entries(lans)[i])
