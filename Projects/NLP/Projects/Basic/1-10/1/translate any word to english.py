from nltk.corpus import swadesh
import nltk


def to_eng(text):
    languages = swadesh.fileids()
    translate = {}
    for i in languages:
        translate.update(swadesh.entries([i, 'en']))
    tokens = nltk.word_tokenize(text)
    eng = ''
    for word in tokens:
        if word in translate:
            eng += ' ' + translate[word]
        else:
            eng += ' ' + word
    return eng


french = """Demain, dès l’aube, à l’heure où blanchit la campagne, Je partirai. Vois-tu, je sais que tu m’attends."""

spanish = """La plaza tiene una torre, la torre tiene un balcón"""

german = """Der du von dem Himmel bist, Alles Leid und Schmerzen stillest"""

texts = [french, spanish, german]
for text in texts:
    print(to_eng(text))
