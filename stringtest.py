
import sys, os, time


array1 = ["abc:eye","abc:brain","abc:leg"]
array2 = ["abc11:eye","abc11:leg","abc11:brain"]

array3 = [None] * len(array1)

i = 0
for a in array3:
	a=array1[i]
	i+=1

with open('your_file.txt', 'w') as f:
    for item in array1:
        f.write("%s\n" % item)

print("abc")