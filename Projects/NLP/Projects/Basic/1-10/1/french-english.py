import nltk
from nltk.corpus import swadesh

french2english = dict(swadesh.entries(['fr', 'en']))
english2french = dict(swadesh.entries(['en', 'fr']))
# print(french2english)
# print(english2french)

original = """This is a book about Natural Language Processing. By “natural language” we mean a
language that is used for everyday communication by humans; languages such as English, Hindi, or Portuguese.
In contrast to artificial languages such as programming languages and mathematical notations, natural languages 
have evolved as they pass from generation to generation, and are hard to pin down with explicit rules."""


def to_french(text):
    tokens = nltk.word_tokenize(text)
    french = ''
    for word in tokens:
        if word.isalpha() and word.lower() in english2french:
            french += ' ' + english2french[word.lower()]
        else:
            french += ' ' + word
    return french


def to_english(text):
    tokens = nltk.word_tokenize(text)
    english = ''
    for word in tokens:
        if word.isalpha() and word.lower() in french2english:
            english += ' ' + french2english[word.lower()]
        else:
            english += ' ' + word
    return english


french = to_french(original)
print('French : ', french)


def evaluate(original):
    print('\n\n\nDoing Back and forth translation between english <-> French')
    english100 = original
    org, eng = '', ''
    for i in range(100):
        french100 = to_french(english100)
        english100 = to_english(french)
    for i in original:
        org += i.strip().lower()
    for i in english100:
        eng += i.strip().lower()
    print("After 100 translations : ")
    value = total = 0
    for i in range(min(len(org), len(eng))):
        total += 1
        if org[i] == eng[i]:
            value += 1
    accuracy = value/total
    print('Accuracy : ', accuracy*100)


evaluate(original)