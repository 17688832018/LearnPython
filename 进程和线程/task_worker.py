#!-*-coding:utf-8 -*-
"""模拟另一台机器启动分布式进程"""

import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 该QueueManger只从网络获取Queue,注册时不用关联本地的Queue对象
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到主进程task_master.py服务器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 验证端口和验证码
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
# 从网路连接
m.connect()
# 获取网络对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列领取任务,并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结果
print('worker exit.')



















