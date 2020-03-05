#验证同一个进程内的所有线程共享全局变量
from threading import  Thread
import time

g_num=1000

def work1():
    global g_num
    while (g_num < 1100):
        g_num+=3
        print("work1----num:",g_num)
        time.sleep(1)

def work2():
    global g_num
    while g_num < 1090:
        print("work2---num:",g_num)
        time.sleep(1)

if __name__ == '__main__':
    print("start---num:",g_num)
    t1=Thread(target=work1)
    t1.start()

    #故意停顿一秒，以保证线程1执行完成
    time.sleep(1)

    t2=Thread(target=work2)
    t2.start()

    # t1.join()
    # t2.join()