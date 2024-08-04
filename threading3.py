'''
    Synchronizing threads & using locking threads.
    
    This allows the threads to wait for another thread to finish before they execute.
    
    There may be some instances where we need to wait for one thread to finish before
    we can move on to another thread.
    
    
    (Example):
    A checkout system with three main functions (each in their own threads): 
        [1. process payment, 2. send conf email, 3. load thank you page]
    
    1. processing payment = 5 seconds
    2. send conf email = 10 seconds
    3. load thank you page = 3 seconds
    
    We can't 2. until 1.
    So 1. must happen before 2. or 3.
    
    In the code we will lock a thread so 2. and 3. only go after 1. 
'''
import threading
import time
###########################################################################
class myThread(threading.Thread):
    def __init__(self, threadId, name, count, delay): 
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
        self.delay = delay
    
    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire() # only allows this thread to run
        print_time(self.name, self.delay, self.count)
        threadLock.release() # allows another thread to start running
        print("Finished: " + self.name + "\n")
###########################################################################
#threadLock release location differs from myThread1
class myThread2(threading.Thread): 
    def __init__(self, threadId, name, count, delay): 
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
        self.delay = delay
    
    def run(self):
        print("Starting: " + self.name + "\n")
        
        # this acquires the lock & checks if any other thread is locked
        threadLock.acquire() 
        threadLock.release()
        
        print_time(self.name, self.delay, self.count)
        
        print("Finished: " + self.name + "\n")
###########################################################################
def print_time(name, delay, count):
    while count: #false at 0
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1
###########################################################################

threadLock = threading.Lock()

thread1 = myThread(1, "Payment Processing", 5, 1)
thread2 = myThread2(2, "Sending Email", 10, 1)
thread3 = myThread2(3, "Loading Page", 3, 1)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("Done main thread")