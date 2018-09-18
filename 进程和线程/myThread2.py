#!-*-coding:utf-8 -*-
"""加入了线程锁
    每当一个线程访问一个共享数据时,将其锁定,同步阻塞,等该线程访问完毕后,再释放锁
    原因例如 balance = balance + n 系统会分为2步计算: x = balance + n,balance = x
    由于x是局部变量,每个线程都有自己的x,当线程交替运行次数足够多时,会出错
"""
import threading
import time


class myThread2(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        # 设置打印间隔 线程执行延迟间隔
        self.counter = counter
    def run(self):
        """加入同步锁"""
        print("开启线程:" + self.name)
        # 获取锁,用于线程同步
        threadLock.acquire()
        print_time(self.name,self.counter,4)
        # 释放锁,开启下一个线程
        threadLock.release()


def print_time(threadName,delay,counter):
    """counter:执行遍历的次数"""
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName,time.ctime(time.time())))
        counter -= 1

# 创建线程锁
threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread2(1,"Thread-1",1)
thread2 = myThread2(2,"Thread-2",2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")





















