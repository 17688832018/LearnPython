#!-*-coding:utf-8 -*-
"""
线程应该使用局部变量,不会影响其他线程,而全局变量修改必须加锁,使用threading.local()实现多线程间的传参
ThreadLocal是全局变量,但每个线程都只能读写自己线程的独立副本,互补干扰
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

"""
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print("Hello,%s (in %s)" % (std,threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()






















