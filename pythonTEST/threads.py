import time,threading

def sub_thread():
    for i in range(10):
        print('thread is running...')
        time.sleep(1)

t = threading.Thread(target=sub_thread,name=None)
t.start()
print('main thread...')

#t.join()