import re

query = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
words = ['language', 'processes', 'processing']
for word in words:
    stem = re.findall(query, word)
    print(stem)
