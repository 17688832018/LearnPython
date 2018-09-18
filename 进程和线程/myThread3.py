#!-*-coding:utf-8 -*-
"""线程优先级队列Queue"""

import threading
import time
import queue


exitFlag = 0


class myThread3(threading.Thread):
    """形参q:对应实参workQueue"""
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程:" + self.name)
        process_data(self.name,self.q)
        print("退出线程:" + self.name)


def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            # .get()读队列 即workQueue.get()
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName,data))
        else:
            queueLock.release()
        time.sleep(1)

# 存放线程的名字,对应myThread3的形参name
threadList = ["Thread-1","Thread-2","Thread-3"]
# 用于填充workQueue队列
nameList = ["One","Two","Three","Four","Five"]
# 创建线程锁
queueLock = threading.Lock()
# 创建一个有10个位置的队列对象
workQueue = queue.Queue(10)
# 列表 用来存放线程对象
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    # 新线程都执行myThread3方法 填充完的队列workQueue实参对应myThread3的形参q
    thread = myThread3(threadID,tName,workQueue)
    thread.start()
    # 往列表里放线程对象,之后通过遍历,给每个线程对象加.join()方法让线程等待至中止
    threads.append(thread)
    # print("线程对象",threads)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    # 往队列里填充数据用put  注意阻塞模式可能导致数据污染 https://www.cnblogs.com/wuxinqiu/p/3862654.html
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")



"""
1. 阻塞模式导致数据污染

import Queue
       q = Queue.Queue(10)
       for i in range(10):
               myData = 'A'
               q.put(myData)
               myData = 'B'

这是一段极其简单的代码，但我总是不能获得期望的结果（期望在队列中写入10个A，却总是混杂了B）。
原来，Queue.put（）默认有 block = True 和 timeou 两个参数。当  block = True 时，写入是阻塞式的，
阻塞时间由 timeou  确定。正因为阻塞，才导致了后来的赋值污染了处于阻塞状态的数据。
Queue.put（）方法加上 block=False 的参数，即可解决这个隐蔽的问题。
但要注意，非阻塞方式写队列，当队列满时会抛出 exception Queue.Full 的异常。

"""














