
import urllib
import xml.etree.ElementTree as ET
#url = "http://python-data.dr-chuck.net/comments_310648.xml"
url = raw_input('File - ')
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
count = 0
xml_sum = 0
for item in lst:
	xml_sum += int(item.find('count').text)
	count += 1

print 'Count: ', count
print 'Sum: ', xml_sum
