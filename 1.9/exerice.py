#!-*-coding:utf-8 -*-
"""P28 1.9编程项目"""
# 1.球半径;直径/周长/面积/体积
import math
def getBall(r):
    d = 2*r
    c = 2*math.pi*r
    s = 4*math.pi*r**2
    v = (4/3)*math.pi*r**3
    print(("d=%.2f,c=%.2f,s=%.2f,v=%.2f")%(d,c,s,v))



# 2.时薪/工时/加班;总周薪
def getSalaryInput(hourlyWage,hours,overtime):
    inputHourlyWage = input(hourlyWage)
    inputHours = input(hours)
    inputOvertime = input(overtime)
    try:
        intHourlyWage = int(inputHourlyWage)
        intHours = int(inputHours)
        intOvertime = int(inputOvertime)
        intWeeklyWage = intHourlyWage * intHours + intHourlyWage * 1.5 * intOvertime
        return intWeeklyWage
    except ValueError:
        print("必须是整数")
        return getSalaryInput(hourlyWage,hours,overtime)

# # 2.
# a =float(input('salary'))
# b =float(input('hours'))
# c =float(input('overtime'))
# print('week',a*b+1.5*a*c)

# 3.弹跳性(bounce=0.2/0.5/0.6时极限为固定整数?)

def getInput(initHeight,count,bounce):
    h = int(input(initHeight))
    c = int(input(count))
    b = float(input(bounce))
    d = 0
    # print("初始高度:%d \n 弹跳次数:%d \n 弹性指数:%f \n" % (h,c,b))
    for i in range(0,c):
        d += h*b**i+h*b**(i+1)
        # print("."*int((h*b**i+h*b**(i+1))))
    return d

# 3.
h=float(input("high"))
t=float(input("times"))
s,b=0,1
while b<t:
    a=h+0.6*h
    h,b=0.6*h,b+1
    s=s+a
print(s)
# 4.
def getPi(count):
    c = int(input(count))
    pi4 = 0.0
    flag = True
    for i in range(1,c+1):
        object1 = 1 / (2 * i - 1)
        # 给i判断奇偶
        if i % 2 == 0:
            pi4 = pi4 - object1
        else:
            pi4 = pi4 + object1

    print("实际结果为:",math.pi/4)
    return pi4



def main():
    # 1.调用第一题方法
    getBall(3.2)
    # 2.测试第二题的方法
    # test1 = getSalaryInput("输入时薪", "输入工时", "输入加班时长")
    # print("Your weeklyWage is", test1)
    # 3.
    # test2 =getInput("输入初始高度","输入次数","输入弹性指数")
    # print("距离为:",test2)
    # 4.
    test4 = getPi("输入迭代次数")
    print("结果为:",test4)




if __name__ == '__main__':
    main()