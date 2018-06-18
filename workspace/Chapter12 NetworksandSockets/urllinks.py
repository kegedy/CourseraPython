# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import re
import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
pos = int(raw_input('Enter position: '))
count = int(raw_input('Repeat # of times: '))
url = "known_by_Xida.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
lst = list()
for i in range(0,count):
	tags = soup('a')
	url = tags[pos-1].get('href',None)
	print url
	lst.append(re.findall('known_by_([^.]+)', url)[0])
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
print lst[len(lst)-1]
