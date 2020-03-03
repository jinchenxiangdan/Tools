
import time
from multiprocessing import Queue, Process
import threading






def function1(MY_QUEUE, lock):
    for i in range(1, 51):
        MY_QUEUE.put(i)
        time.sleep(0.1)
        print("Inserting ", i, "...")
    lock.acquire()
    IS_INPUT_DONE = True
    lock.release()

def function2(MY_QUEUE, lock):
    while not IS_INPUT_DONE:
        while not MY_QUEUE.empty():
            print(MY_QUEUE.get())
        print("Lock is: ", IS_INPUT_DONE)
        

    print("Done")







global IS_INPUT_DONE



if __name__ == "__main__":
    lock = threading.Lock()

    IS_INPUT_DONE = False
    print("Multithread testing start...")
    MY_QUEUE = Queue()
    p1 = Process(target=function1, args=(MY_QUEUE, lock,))
    p1.start()
    p2 = Process(target=function2, args=(MY_QUEUE, lock,))
    p2.start()

