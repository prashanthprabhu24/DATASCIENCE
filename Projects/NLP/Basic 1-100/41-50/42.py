from nltk.corpus import webtext

print(webtext.fileids())

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65])
