# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   ## Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs


import urllib
from BeautifulSoup import *
#url = raw_input("Enter - ")
url = "comments_310651.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags  = soup('span')
sum = 0
for tag in tags:
	sum = sum + int(tag.contents[0])
print sum


