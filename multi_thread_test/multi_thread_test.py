
import time
from multiprocessing import Queue, Process
import threading


def function1():
    global MY_QUEUE, IS_INPUT_DONE,lock
    for i in range(1, 51):
        print("Inserting ", i, "...")
        MY_QUEUE.put(i)
        time.sleep(0.1)
    lock.acquire()
    print(lock.locked())
    IS_INPUT_DONE = True
    lock.release()
    print(lock.locked())
    print("Value is: ",IS_INPUT_DONE)


def function2():
    global MY_QUEUE, IS_INPUT_DONE,lock
    while not IS_INPUT_DONE:
        while not MY_QUEUE.empty():
            print(MY_QUEUE.get())
        # print("IS INPUT DONE is: ", IS_INPUT_DONE)

        
    print("Done")


if __name__ == "__main__":
    lock = threading.Lock()
    IS_INPUT_DONE = False
    MY_QUEUE = Queue()

    print("Multithread testing start...")

    p1 = Process(target=function1)
    p1.start()
    p2 = Process(target=function2)
    p2.start()

    p1.join()
    p2.join()

