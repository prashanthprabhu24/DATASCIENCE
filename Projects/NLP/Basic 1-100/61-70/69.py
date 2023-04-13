from nltk.corpus import swadesh

# en to fr
en2fr = swadesh.entries(['en', 'Fr'])
print(en2fr)

translate = dict(en2fr)
print(translate['dog'])

