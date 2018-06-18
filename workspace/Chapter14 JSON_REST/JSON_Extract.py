
import urllib
import json
#url = raw_input("File - ")
url = "http://python-data.dr-chuck.net/comments_310652.json"
print "Retrieving", url
string = urllib.urlopen(url).read()
print "Retrieved", len(string), "characters"
struct_data = json.loads(string)

comments = struct_data["comments"]
count = 0
comment_sum = 0
for comment in comments:
	comment_sum += int(comment["count"])
	count += 1
print "Count:", count
print "Sum:", comment_sum
