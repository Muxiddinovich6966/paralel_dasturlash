import time,os
from asyncio import sleep
from itertools import count
from threading import Thread, current_thread
from multiprocessing import Process,current_process
from vazifa_2 import *

count=100_000_000
sleep=5




def read_fayl(vazifa_2):
    p_id = os.getpid()
    print(f"{p_id}---{current_process().name}---{current_thread().name}----kutush boshlandi")

    with open(vazifa_2, "r") as file:
        time.sleep(sleep)
        f = file.read()
        print(f"{p_id}---{current_process().name}----{current_thread().name}----kutush yakunlandi")

        return f
    # print(f"{p_id}---{current_process().name}----{current_thread().name}----kutush yakunlandi")
#
# def cpu_b(k):
#     p_id=os.getpid()
#     print(f"{p_id}---{current_process().name}----{current_thread().name}----hisoblash boshlandi")
#     while k>0:
#         k-=1
#         print(f"{p_id}---{current_process().name}----{current_thread().name}----hisoblash yakunlandi")
#

# def read_fayl(vazifa_2):
#     with open(vazifa_2,"r") as file:
#         f=vazifa_2()
#     return f

if  __name__=="__main__":
    s_time=time.time()
    # 1 single threed  io_b   vaqt 10.000675439834595
    # io_b(sleep)
    # io_b(sleep)

    # 2 chisi multithreed - io_b   vaqt 5.00234580039978
    # t1=Thread(target=io_b,args=(sleep,))
    # t2=Thread(target=io_b,args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()


    # 3 singletheed cpu_b
    # cpu_b(count)
    # cpu_b(count)
    #
     # 4 multithreed cpu_b  vaqt 5.002312421798706
    # t1 = Thread(target=io_b, args=(count,))
    # t2=Thread(target=io_b,args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 5 vaqt 5.565915822982788
    t1 = Process(target=read_fayl, args=("vazifa_2.py",))
    t2=Process(target=read_fayl,args=("vazifa.py",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    e_time=time.time()
    print("vaqt=", e_time-s_time)


    # 5 multiprocessing cpu_b vaqt 5.331284284591675
