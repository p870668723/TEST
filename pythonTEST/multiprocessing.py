import os
import signal
import time
import Queue

print(os.getpid())
pid = os.fork()
q = Queue.Queue(100)

if pid==0:
    print("This is child(%s) processing..."%(os.getpid()))
    c = 0
    with open('./log.txt','w') as f:
            while(True):
                c=c+1
                f.write('%s \n'%c)
                if c>100:
                    f.close()
                    break
else:
    print('This isparent(%s) processing...'%(os.getpid()))
    os.kill( os.getpid() ,signal.SIGKILL)
    