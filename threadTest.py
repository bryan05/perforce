#!/usr/bin/python

import queue
import threading
import time
import os
from shutil import copyfile
exitFlag = 0

files = []



queueLock = threading.Lock()

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
        global processedFiles
        processedFiles=0
        for file in files:
            sourcefilepath=os.path.join("test", file)
            destfilePath = os.path.join("test2", file)
            #queueLock.acquire()
            processedFiles+=1
            #queueLock.release()
            copyfile(sourcefilepath, destfilePath)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)


class FileManager :
    def __init__(self):
        pass

    def copyfiles(self):
        totalNum=0
        for dirpath, dirnames, filenames in os.walk("test"):			
            for filename in filenames:
                files.append(filename)
                totalNum+=1
       
        thread = myThread(1, "test", "")
        thread.start()

        while 1:
           # queueLock.acquire()
            if totalNum!= processedFiles:
                pass
            else:
                break
            #queueLock.release()
            print ("processing %d" % (processedFiles))
        thread.join()

    def runThread(self):
        threadList = ["Thread-1"]
        nameList = ["One", "Two", "Three", "Four", "Five"]
        queueLock = threading.Lock()
        workQueue = Queue.Queue(10)
        threads = []
        threadID = 1

        # Create new threads
        for tName in threadList:
           thread = myThread(threadID, tName, workQueue)
           thread.start()
           threads.append(thread)
           threadID += 1

        # Fill the queue
        queueLock.acquire()
        for word in nameList:
           workQueue.put(word)
        queueLock.release()

        # Wait for queue to empty
        while not workQueue.empty():
           pass

        # Notify threads it's time to exit
        exitFlag = 1

        # Wait for all threads to complete
        for t in threads:
           t.join()
        

fileManager= FileManager()
fileManager.copyfiles()
print ("Exiting Main Thread")