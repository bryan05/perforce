
import sys,os,re
from collections import defaultdict

def testDic () :
    dic = defaultdict(list)

    dic["abc"].append("1")
    dic["abc"].append("2")
    dic["def"].append("3")
    dic["def"].append("4")
    dic["def"].append("5")


    #a=["a","b","c"]
    #print(dic)
    #for x in dic.items():
    #    for y in range(len(x)):
    #        print(x[y])

    #for y in range(len(a)):
    #    print(a[y])

    for x in dic:
        print (x)
        l= dic[x]
        for y in range(len(l)):
            print (y,':',l[y])

    print("done")

def testReg():
    name = "s010_battle"
    shot_pattern = r's([0-9]+)(_|-)*'
    number_pattern = r'[1-9][0-9]*'
    taskName = re.sub(shot_pattern,r'',name)
    #m = re.match(shot_pattern,name)

    m = re.search(number_pattern,name)
    if m is not None:
        numberStr =m.group(0)




shot_pattern = r's(_|-)*([0-9]+)(_|-)*'
number_pattern = r'[1-9][0-9]*'
redundant_pattern = r'(_|-)*'
def isShotDirEqual(str = "", dir =""):
	m1 = re.search(shot_pattern,str)
	m2 = re.search(shot_pattern,dir)
	if m1 is None or m2 is None:
		return False
	m = re.search(number_pattern,dir)
	if m is not None:
		dirNumberStr =m.group(0)
	else:
		return False
	m = re.search(number_pattern,str)
	if m is not None:
		shotNumberStr =m.group(0)
	else:
		return False
	if dirNumberStr == shotNumberStr:
		return True
	return False

#isShotDirEqual(str = "s-010", dir ="s010")

def getNameStrs(str, nameList):
    m = re.search(shot_pattern,str)
    if m is not None:
        shotname= m.group(0)
        shotname = re.sub(redundant_pattern,r'',shotname)
        nameList.append( shotname)

    else:
        return 
    taskName = re.sub(shot_pattern,r'',str)
    nameList.append( taskName)


class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        if self.abc is not None:
            print("changed")


#python =Snake("Python")


#nameList=[]
#getNameStrs("s010-battle",nameList)

#python.change_name("aaaa")

print("done")