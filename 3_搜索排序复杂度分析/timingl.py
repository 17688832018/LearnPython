"""
测试运行时间 用简单循环/嵌套(nested)循环
"""
import time

problemSize = 10000000
print("%12s%16s" % ("Problem Size","Seconds"))
for count in range(5):
    # 迭代次数
    number = 0
    # 返回1970.1.1至今的时间戳 单位:秒
    start = time.time()
    start2 = time.clock()
    work = 1
    # 测试程序

    for x in range(problemSize):
        # for y in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # 程序运行时间
    elapsed = time.time() - start
    # cpu运行时间
    elapsed2 = time.clock() -start2
    print("%12d%16.3f" % (problemSize,elapsed))
    print("%12d%16.3f" % (problemSize,elapsed2))

    problemSize *= 2