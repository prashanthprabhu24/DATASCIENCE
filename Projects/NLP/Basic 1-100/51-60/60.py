import nltk


def content_fraction(text):
    stopwards = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwards]
    return len(content) / len(text)


print(content_fraction(nltk.corpus.reuters.words()))