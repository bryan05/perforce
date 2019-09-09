

import os
#myCmd = 'ls -la'
#os.system(myCmd)
fileRoot="D:\\p4\\2019.1_galaxy\\UnrealEngine\\Engine"
wildcards = r"@#%*"

def forceAdd() :
    i=1
    for dirpath, dirnames, filenames in os.walk(fileRoot):
            for filename in filenames:
                #print ('p4 -u bryan.y -P 9122 add -c 5708 -f "2019.1_galaxy/UnrealEngine/Engine/Extras/Instruments/%UE4 System Trace.tracetemplate"')
                filePath = os.path.join(dirpath, filename)
                myCmd = 'p4 -u bryan.y -P 9122 add -c 5708 -f "'+filePath+'"'
                #if any(elem in filePath for elem in wildcards) :
                    #print(filePath)
                os.system(myCmd)
                i+=1
    print("total number:"+ str(i))

def changeFileTypes():
    dirs= ["Binaries","Build","Documentation","Extras","Intermediate","Plugins"]
    subFolder= "Plugins\\"
    for dir in dirs:
        taskFolder= os.path.join(fileRoot, dir)
        i=1
        for dirpath, dirnames, filenames in os.walk(taskFolder):
                for filename in filenames:
                    #print ('p4 -u bryan.y -P 9122 add -c 5708 -f "2019.1_galaxy/UnrealEngine/Engine/Extras/Instruments/%UE4 System Trace.tracetemplate"')
                    filePath = os.path.join(dirpath, filename)
                    myCmd = 'p4 -u bryan.y -P 9122 add -c default -t binary  "'+filePath+'"'
                    #if any(elem in filePath for elem in wildcards) :
                        #print(filePath)
                    os.system(myCmd)
                    i+=1
    print("total number:"+ str(i))

def changeFileTypesSingleFolder():
    subFolder= "Content\\Internationalization\\"
    taskFolder= os.path.join(fileRoot, subFolder)
    i=1
    for dirpath, dirnames, filenames in os.walk(taskFolder):
            for filename in filenames:
                #print ('p4 -u bryan.y -P 9122 add -c 5708 -f "2019.1_galaxy/UnrealEngine/Engine/Extras/Instruments/%UE4 System Trace.tracetemplate"')
                filePath = os.path.join(dirpath, filename)
                myCmd = 'p4 -u bryan.y -P 9122 reopen -c 5742 -t binary  "'+filePath+'"'
                #if any(elem in filePath for elem in wildcards) :
                    #print(filePath)
                os.system(myCmd)
                i+=1
    print("total number:"+ str(i))

def changeFileTypesToUni():
    dirs= ["Config","Content"]
    subFolder= "Plugins\\"
    for dir in dirs:
        taskFolder= os.path.join(fileRoot, dir)
        i=1
        for dirpath, dirnames, filenames in os.walk(taskFolder):
                for filename in filenames:
                    #print ('p4 -u bryan.y -P 9122 add -c 5708 -f "2019.1_galaxy/UnrealEngine/Engine/Extras/Instruments/%UE4 System Trace.tracetemplate"')
                    filePath = os.path.join(dirpath, filename)
                    myCmd = 'p4 -u bryan.y -P 9122 reopen -c default -t utf16  "'+filePath+'"'
                    # text,utf16
                    #if any(elem in filePath for elem in wildcards) :
                        #print(filePath)
                    os.system(myCmd)
                    i+=1
    print("total number:"+ str(i))


def addFileToPerforce():
    dirs= ["Source","Intermediate"]
    subFolder= "Plugins\\"

    taskFolder= os.path.join(fileRoot, subFolder)
    i=1
    for dirpath, dirnames, filenames in os.walk(taskFolder):
        temp_dirs=dirpath.split("\\")
        IsDeleted=False
        for temp_dir in temp_dirs:
            if temp_dir == dirs[0] or temp_dir == dirs[1] :
                IsDeleted=True

        if not IsDeleted :
            for filename in filenames:
                #print ('p4 -u bryan.y -P 9122 add -c 5708 -f "2019.1_galaxy/UnrealEngine/Engine/Extras/Instruments/%UE4 System Trace.tracetemplate"')              
                filePath = os.path.join(dirpath, filename)
                myCmd = 'p4 -u bryan.y -P 9122 add -c default "'+filePath+'"'
                # text,utf16
                #if any(elem in filePath for elem in wildcards) :
                    #print(filePath)
                os.system(myCmd)
                i+=1
    print("total number:"+ str(i))

def submitAborted() :
     myCmd = 'p4 -u bryan.y -P 9122 submit -c 5708'
     os.system(myCmd)

def reopen():
    subFolder= "Binaries\\"
    taskFolder= os.path.join(fileRoot, subFolder)
    myCmd = 'p4 -u bryan.y -P 9122 reopen -c default "'+taskFolder+'"'
    os.system(myCmd)

reopen()
#addFileToPerforce()
#changeFileTypesToUni()
print("finished")