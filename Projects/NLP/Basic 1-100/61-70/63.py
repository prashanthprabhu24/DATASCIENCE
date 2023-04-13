from nltk.corpus import names
import nltk

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid)
)

cfd.tabulate()
cfd.plot()
