Text Translation using Swadesh Corpus from NLTK

NLTK includes so-called Swadesh wordlists, lists of about 200 common words in several languages.

>> from nltk.corpus import swadesh
                    >> swadesh.fileids() # for listing language options
                    >> swadesh.words('en') # for listing all words in English
                    >> fr2en = dict(swadesh.entries(['fr', 'en']) # for french to english translations.

