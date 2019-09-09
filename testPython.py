

import sys, os, time
from collections import defaultdict

global dic
dic = defaultdict(list)

def test1():
	array1 = ["abc:eye","abc:brain","abc:leg"]
	array2 = ["abc11:eye","abc11:leg","abc11:brain"]

	array3 = [None] * len(array1)

	i = 0
	for a in array1:
		name = a.rsplit(":")[0]
		dic[name]=i
		i+=1


	for a in array2:
		name = a.split(":")[1]
		if name in dic:
			value=dic[name]
			array3[value]=a


	with open('your_file.json', 'w') as f:
		for item in array1:
			f.write("%s\n" % item)

str="X:\Projects\GM_20190318_GalaxyMobile\3d\03_Sequence\Shots\GM-0070\Export\_ShotCam\v0004_AssetSwap&Export_bya\centimeter\shot_GM-0070_ShotCam_v0004"
str1=str.split("\_ShotCam")[0]
str2=str1+"\_ShotCam"
#i = 0
#for a in array1:
#	array3[i]=a
#	i+=1


print("abc")