import multiprocessing as mtp
import os
import time

def func(msg):
    while True:
        print os.getpgid(0)
        #print msg
        #time.sleep(0.1)

if __name__ == "__main__":
    p = mtp.Process(target=func, args=("hello",))
    y = mtp.Process(target=func, args=("hello",))
    p.start()
    #y.start()
    
    p.join()
    #y.join()
    print "finished"