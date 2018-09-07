#!-*-coding:utf-8 -*-
"""类的结构和理解"""
class Counter(object):
    # Counter对象(类对象)的数量
    instance = 0
    # self即this,谁调用了该方法(如Counter.c1实例调用了increment方法),指向谁(c1),即此时的self=c1,
    # c1指向Counter的实例化对象,self此时也指向Counter的实例化对象
    def __init__(self):
        """
        构造方法(创建实例化对象时会被自动调用)
        建立计数器
        """
        # 更新了对象数量
        Counter.instance +=1
        # 初始化单个实例变量(创建该self的时候对其初始化)
        self.reset()

    # mutator 修改器方法(修改变量的值/状态)
    def reset(self):
        self._value = 0

    def increment(self,amount = 1):
        self._value += amount

    def decrement(self,amount = 1):
        self._value -= amount

    # accessor存取器访问器方法(不修改变量的值)
    def getValue(self):
        return self._value

    # 自动继承object的方法 重写
    # 当print时会自动调用__str__方法
    def __str__(self):
        return str(self._value)
    # 当==时会调用__eq__方法(值相等)
    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._value == other._value


# test
c1 = Counter()
print(c1)
c1.increment(12)
print(c1)