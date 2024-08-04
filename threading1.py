'''
    (Context):
    The threading module in Python allows for concurrent execution of tasks. 
    
    When you use time.sleep(delay) within a thread, 
    it causes the current thread to suspend its execution for the specified delay seconds.
 
    During this time, the Python interpreter does not just sit idle; instead, it can execute other threads.

    (Program):
    Starting at counter = 5, count down to 0
'''
import time
import threading
################################################
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        print("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "\n")
################################################
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n")
        counter -= 1
################################################
#Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

#Start new threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
