
import time
from multiprocessing import Queue
from threading import Thread, Lock


lock = Lock()
IS_INPUT_DONE = False
MY_QUEUE = Queue()
COUNT = 0;

def function1():
    global MY_QUEUE, IS_INPUT_DONE,lock, COUNT
    for i in range(1, 51):
        print("Inserting ", i, "...")
        MY_QUEUE.put(i)
        time.sleep(0.1)
    lock.acquire()
    print(lock.locked())
    IS_INPUT_DONE = True
    COUNT+=1
    lock.release()
    print(lock.locked())
    print("Thread 1-",COUNT,": IS_INPUT_DONE is: ",IS_INPUT_DONE)


def function2():
    global MY_QUEUE, IS_INPUT_DONE,lock, COUNT
    while not IS_INPUT_DONE:
        while not MY_QUEUE.empty():
            print(MY_QUEUE.get())
        print("Thread 2-",COUNT,": IS INPUT DONE is: ", IS_INPUT_DONE)
        lock.acquire()
        # COUNT+=1
        lock.release()
        time.sleep(1)

        
    print("Done")



if __name__ == "__main__":

    print("Multithread testing start...")

    p1 = Thread(target=function1)
    p1.start()

    p2 = Thread(target=function2)
    p2.start()

    p1.join()
    p2.join()

    while not IS_INPUT_DONE:
        time.sleep(1)
        print("Thread main-",COUNT,": is input done: false")
        
    print("Thread main-: IS_INPUT_DONE: True")
