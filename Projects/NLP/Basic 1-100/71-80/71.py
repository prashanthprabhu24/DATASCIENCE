from urllib.request import urlopen

url = "https://www.gutenberg.org/files/2554/2554-0.txt"
raw = str(urlopen(url).read())
print(len(raw), type(raw))
print(raw[:75])
