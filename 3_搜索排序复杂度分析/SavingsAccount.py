class SavingsAccount(object):
    """
    自定义某种数据项的 比较算法
    """
    # 传入名称 pin码 余额 通过名称比较
    def __init__(self,name,pin,balance=0.0):
        self._name = name
        self._pin =pin
        self._balance =balance


    def __lt__(self, other):
        return self._name < other._name


s1 = SavingsAccount('Ken','1000',0)
s2 = SavingsAccount('Bill','1001',30)
print(s1<s2)