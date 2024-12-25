import time,os
from multiprocessing import Process,current_process
from threading import Thread, current_thread




def list_work(a:list):

    p_id=os.getpid()
    print(f"{p_id}----{current_process().name}---{current_thread().name}----Jarayon boshlandi")
    juft=1
    toq=1
    yigindi=0
    time.sleep(5)
    for i in a:
        if i%2==0:
            juft*=i
        elif i%2==1:
            toq*=i

    print(f"natija == {(juft-toq)}")
    print(f"{current_process().name} ---- {current_thread().name} --- jarayon yakunlandi")


if  __name__=="__main__":
    d = list(range(1, 40))
    s_time=time.time()
# 1 single threed  vaqt= 10.001343965530396
    # list_work(d)
    # list_work(d)

# 2 multithreed   vaqt= 5.001986980438232
    # f1=Thread(target=list_work,args=(d ,))
    # f2=Thread(target=list_work,args=(d ,))
    # f1.start()
    # f2.start()
    #
    # f1.join()
    # f2.join()

# 3 multiprogres   vaqt= 5.181861400604248
    m1=Process(target=list_work,args=(d ,))
    m2=Process(target=list_work,args=(d ,))

    m1.start()
    m2.start()

    m1.join()
    m2.join()
    e_time=time.time()
    print("vaqt=", e_time-s_time)

