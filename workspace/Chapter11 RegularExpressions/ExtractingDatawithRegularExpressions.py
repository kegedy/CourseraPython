#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
name = raw_input("Enter file:")
hand = open(name)
sum = 0
for line in hand:
	array = re.findall('[0-9]+',line)
	for number in array:
		sum = sum + int(number)
		
print sum
