#!/usr/bin/env python2
import threading
import time
class MyThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting : " + self.name)
		threadLock.acquire()
		print_time (self.name, 5, self.counter)
		threadLock.release()
def print_time(threadName, counter, delay):
	while counter:
		time.sleep(delay)
		print ("%s : %s" %(threadName, time.ctime(time.time())))
		counter -= 1
threadLock = threading.Lock()
threads = []
thread1 = MyThread(1, "Thread-1",1)
thread2 = MyThread(2, "Thread-2",2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
	t.join()
print ("Exiting the main thread.")
