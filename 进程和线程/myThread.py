#!-*-coding:utf-8 -*-
import threading
import time


exitFlag = 0


class myThread(threading.Thread):
    """继承自threading.Thread
        重写了 初始化方法 和 运行方法
        该线程体的内容为:打印了2行内容,调用了一个自定义的print_time方法
    """
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter =counter

    # run(): 调用run()来完成线程体的运行,包含了要执行的这个线程的内容
    def run(self):
        print("开始进程:" + self.name)
        print_time(self.name,self.counter,5)
        print("退出线程:" + self.name)


def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        # time.ctime(将括号里的时间转换为字符串格式的时间)
        print("%s:%s" %(threadName,time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

# 开始新线程
# start():启用一个线程(表明该对象是一个线程,不是单纯的调用run()方法)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")


































