'''
    When you want to create a new thread, 
    you must create a subclass of the main thread class from the threading module.
    
    In order to create different kinds of threads, create more classes like 'myThread2' etc.
    & change the function inside the run() method.
'''
import threading
import time
###########################################################################
class myThread(threading.Thread):
    # reason for count is the thread we make will count down that number.
    def __init__(self, threadId, name, count, delay): 
        #First thing, call the parent constructor method
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
        self.delay = delay
    
    # must be caled 'run' which defines what the thread does
    def run(self):
        print("Starting: " + self.name + "\n")
        #func that what the thread is/does
        print_time(self.name, self.delay, self.count)
        print("Exiting: " + self.name + "\n")
###########################################################################
def print_time(name, delay, count):
    while count: #false at 0
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1
###########################################################################

thread1 = myThread(1, "Thread1", 10, 1)
thread2 = myThread(2, "Thread2", 5, 2)
thread3 = myThread(3, "Thread3", 7, 0.5)

thread1.start()
thread2.start()
thread3.start()
#Waits for the threads finish executing before terminating the program
thread1.join()
thread2.join()
thread3.join()
print("Done main thread")