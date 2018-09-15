"""
探索 指令计数的增长
"""
# import sys
# print(sys.path)
# sys.path.append('G:\\pythonPro\\LearnPython\\3_1')

from counter import Counter

def fib(n,counter):
    counter.increment()
    if n<3:
        return 1
    else:
        return fib(n-1,counter) + fib(n-2,counter)


problemSize = 2
print("%12s%15s" % ("ProblemSize","Calls"))
for count in range(5):
    # 迭代调用的次数
    counter = Counter()
    fib(problemSize,counter)
    print("%12d%15s" % (problemSize,counter))
    problemSize *= 2
