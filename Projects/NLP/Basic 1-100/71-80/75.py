import feedparser

llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print(llog['feed'])
print(len(llog.entries))
post = llog.entries[2]
print(post.title)
content = post.content[0].value
print(content[:50])

