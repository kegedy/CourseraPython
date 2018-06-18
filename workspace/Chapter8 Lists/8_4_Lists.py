#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

#fname = raw_input("Enter file name: ")
try:
    fh = open("romeo.txt")
except:
    print "Not found"
    exit()
lst = list()
words = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if len(lst) == 0 or word not in lst:
            lst.append(word)
lst.sort()                
print lst