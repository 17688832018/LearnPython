#!-*-coding:utf-8 -*-
"""先启动主线程,创建分布式进程,再在task_worker中启动进程"""
import random,time,queue
from multiprocessing.managers import BaseManager

# 创建发送任务的队列:
task_queue = queue.Queue()
# 创建接收结果的队列:
result_queue = queue.Queue()

# 继承
class QueueManger(BaseManager):
    pass

# win10环境下 PermissionError OSError
# pickle模块不能序列化lambda函数,需要自定义task_queue和result_queue
# def return_task_queue():
#     global task_queue
#     return task_queue
# def return_result_queue():
#     global result_queue
#     return result_queue
#
# QueueManager.register('get_task_queue',callable=return_task_queue)
# QueueManager.register('get_result_queue',callable=return_result_queue)

# 将队列注册到网络 callable参数关联了本地Queue对象 之后在分布式多进程环境下调用get_task_queue()获得的Queue接口调用原始queue
QueueManger.register('get_task_queue',callable=lambda:task_queue)
QueueManger.register('get_result_queue',callable=lambda:result_queue)
# 绑定端口5000,验证码为abc
manager = QueueManger(address=('127.0.0.1',5000),authkey=b'abc')
manager.start()
# 通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭
manager.shutdown()
print('master exit.')






































