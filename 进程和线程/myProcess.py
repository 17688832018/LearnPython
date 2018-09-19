#!-*-coding:utf-8 -*-
"""进程:基于操作系统

Python由于设计的GIL锁,不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

linux系统:
    fork() 调用一次返回两次,操作系统会自动把当前进程(父进程)复制了一份(子进程),
    然后分别在父进程和子进程内返回,
    子进程永远返回 0 通过getppid()获取父进程的ID
    父进程返回子进程的ID
跨平台:
    使用multiprocessing模块
"""
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import os,time,random,subprocess
from multiprocessing import Process,Pool,Queue
# multiprocess模块下的Queue方法常用于 一个父进程和他的子进程相互之间的通信 各子进程共有
# 直接import queue 这个模块 用于多个进程之间的通信 各自私有

# # os.fork()创建进程
# print("Process (%s) start..." % os.getpid())
# pid = os.fork()
# # 子进程永远返回0
# if pid == 0:
#     print("I am child process (%s) and my parent is %s" % (os.getpid(),os.getppid()))
# else:
#     print("I (%s) just created a child process (%s)" % (os.getpid(),pid))

# 跨平台创建进程
# 子进程里要执行的代码
def run_proc(name):
    print("Run child process %s (%s)..." % (name,os.getpid()))


# 进程池创建的进程运行时间(放在apply_async中)
def long_time_task(name):
    print("进程池 Run task %s (%s)..." % (name,os.getpid()))
    start = time.time()
    # random.random()生成0-1之间的随机浮点数
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name,(end-start)))


# 进程间通信 通过Queue Pipes等实现交换数据
# 写数据
def write(q):
    print("Process to write:%s" % os.getpid())
    for value in ['A','B','C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

# 读数据
def read(q):
    print("Process to read:%s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == '__main__':
    # print("Parent process %s." % os.getpid())
    # # 创建一个Process进程实例
    # p = Process(target=run_proc,args=('test',))
    # print("Child process will start.")
    # # 启动进程 区别与线程
    # p.start()
    # # 等待子进程结束后再继续往下运行,常用语进程之间的同步
    # p.join()
    # print("Child process end.")
    #
    # # 进程池批量创建子进程
    # print("进程池批量创建子进程 Parent process %s." % os.getpid())
    # # 与cpu核心有关
    # p = Pool(4)
    # for i in range(5):
    #     # apply_async()异步非阻塞执行:不用等待当前进程执行完毕,随时根据系统调度切换进程 区别与apply()的串行执行(废弃)
    #     # args中是元组格式
    #     p.apply_async(long_time_task,args=(i,))
    # print("Waiting for all subprocesses done...")
    # # 调用join前必须先调用close(),调用close()后就不能继续添加新的Process了
    # p.close()
    # p.join()
    # print("All subprocesses done")
    # subprocess启动一个子进程
    # print("$ nslookup www.python.org")
    # r = subprocess.call(['nslookup','www.python.org'])
    # print('Exit code:',r)
    # communicate()输入
    # print("$ nslookup")
    # p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode('utf-8'))
    # print('Exit code:',p.returncode)

    # 进程间通信
    # 父进程创建Queue(q对象),并传给各个子进程(pw和pr对象):
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr进程里是死循环,无法等待其结束,强行终止
    pr.terminate()




































