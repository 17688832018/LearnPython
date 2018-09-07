#!-*-coding:utf-8 -*-
def main():
    # 10! while条件
    value = 1
    product = 1
    while value<11:
        product *= value
        value+=1
    print(product)
    # 10! for循环
    product = 1
    for value in range(1,11):
        product*=value
    print(product)
    # 字符串比较(通过ASCII码值来比较)
    a,b,A = 'a','b','A'
    print(A<a,a<b)
    # 字符串索引
    c = "abcde"
    print(c[2])
    print("abcdef"[2:5])
    # 格式化字符串
    # for i in range(7,11):
    #     print(str(i)+':',10 ** i)
    # 对齐%-4d表示第一列数字在初始宽度为4的字段中左对齐
    # "%s"       表示字符串
    # "%-s"     表示左对齐的字符串
    # "%-12s"   表示左对齐初始宽度为12的字符串
    # "%-10.5f" 表示左对齐初始宽度为10精度为5的浮点数
    for i in range(7,11):
        # print("格式" % "内容")
        # print("%-4s" % "12asd")
        # print("%-4d %12d" % (i,10**i))
        print("%-4s%12d" % (str(i)+':',10**i))
    print("Your salary is $ %0.5f" % 1000)
    print("Your salary is $"+"%0.2f",2000)
    # 要求:左对齐 宽度10 精度5来格式化3.14
    print("%-10.5f" % 3.14)  # 结果为:3.14000   ; 宽度不给或给的小也会被撑大
    print("greater".isupper())
    print("greater".upper())
    print("greater".startswith("great"))  # .startswith("")不分大小写
    # dir用来返回某对象能识别的所有方法
    print(dir(str))

    # 列表
    testList = ['j','J','2j','0j','j0','j-1','j1','-j','@#','*','(aasd45','\\']
    testList.append('34')
    testList.append('22')
    # sort用于int排序
    testList.sort()
    print(testList)
    # pop获取断尾
    # print(testList.pop())
    print(testList)
    # insert索引前插入
    testList.insert(3,'x')
    print(testList)
    # index获取指定元素的索引
    # print(testList.index('x'))
    # pop截取出索引为2的元素
    # print(testList.pop(2))
    print(testList)
    # remove删除'2j'元素
    testList.remove('2j')
    print(testList)
    print(testList[2:5])
    print(testList)
    # 不同于js的split和join
    # split 以...分割 不能为空
    print("P.yt.hon.iscool".split('.'))
    # join 合并列表/加入 可为空
    print('.'.join("asdfg"))  # a.s.d.f.g
    print(''.join(['a','b','e']))  # abe
    # 遍历索引
    list1 = [23,23,233]
    for i in range(len(list1)):
        print(i)
    # 字典
    dic1 = {'name':123,'age':2}
    print(dic1.keys())
    print(dic1.values())
    # 模式匹配
    """将获取返回得到的一个元组((234,123,120),'bgColor') 一次性分别传递过来
    第一项为嵌套的元组rgb颜色,第2项为字符串"""
    rgbTuple = ((234,123,120),'bgColor')
    ((r,g,b),colorName) = rgbTuple
    # def练习
    def square(n):
        """传入n,返回n的平方"""
        square = n**2
        # 没有return 会默认返回none
        return square
    print(square(30))

    # 递归函数:调用自身 至少一条if 避免无限调用自身
    def displayRange(lower,upper):
        """递归函数写法"""
        if lower < upper:
            print(lower)
            displayRange(lower+1,upper)

    displayRange(3,10)

    def displayRange2(lower,upper):
        """非递归写法"""
        while lower < upper:
            print(lower)
            lower += 1

    displayRange2(12,16)

    def ourSum (lower,upper):
        """递归求和"""
        if upper > lower:
            return 0
        else:
            return lower + ourSum(lower+1,upper)

    ourSum(16,23)

    # 高阶函数
    # 列表复制
    oldList =[6,12,52,41,523,1,-5,-9]
    newList = []
    for i in oldList:
        newList.append(str(i))
    print(newList)
    # list(map(def,object))
    newList2 = []
    newList2 = list(map(str,oldList))
    print(newList2)
    def isPositive(a):
        if a >0:
            return a
    # list(filter(isBoolean,object))
    newList3 = list(filter(isPositive,oldList))
    print(newList3)

    # lambda匿名函数(一次性)
    newList4 = list(filter(lambda a:a>0,oldList))
    print(newList4)
    # 用带有2个参数的函数将对象转换为单个的值
    import functools
    product2 =functools.reduce(lambda x,y:x*y,range(1,11))
    print(product2)

    # 捕获异常
    def safeintegerInput(prompt):
        """键入number 异常处理"""
        inputString = input(prompt)
        try:
            number = int(inputString)
            return number
        except ValueError:
            print("Error in number format",inputString)
            return safeintegerInput(prompt)
    # 调用safeintegerInput
    age = safeintegerInput("enter your age please")
    print("your age is :",age)

    # 写文件
    f = open("myfile.txt","w")
    f.write("First line. \nSecond line. \n")
    f.close()

    #
    import random
    f2 = open("integers.txt","w")
    for i in range(500):
        # 获取1-500随机整数
        number = random.randint(1,500)
        f2.write(str(number) + "\n")
    f2.close()

    f22 = open("integers2.txt",'w')
    for i in range(500):
        number = random.randint(1,500)
        f22.write(str(number) + "\t")
    f22.close()

    # 读文件
    f3 =open("myfile.txt",'r')
    text = f3.read()
    print(text)
    # readline
    f4 = open("myfile.txt",'r')
    line = f4.readline()
    if line != "":
        print(line)
    # 读取文件中的数字
    f5 = open("integers.txt",'r')
    sum = 0
    for line in f5:
        # 用.strip()删除换行符
        line = line.strip()
        number = int(line)
        sum += number
    print("the sum is",sum)
    # 读取空格为间隔的内容
    f6 = open("integers2.txt",'r')
    sum = 0
    for line in f6:
        wordlist =line.split()
        for word in wordlist:
            number = int(word)
            sum += number
    print("the sum is",sum)
    # pickle实现读写对象
    """
      pickle目的不是让人来读的，如果你需要类似 ['apple', 'carrot']这样的，可以使用json模块。
      
    """
    import pickle
    lyst = [23,"sad",32,"aa"]
    fileObj = open("item.dat","wb")
    for i in lyst:
        # 1 表示ASCII码
        pickle.dump(i,fileObj,1)
    fileObj.close()
    # pickle读
    lyst2 = list()
    fileObj2 =open("item.dat","rb")
    while True:
        try:
            item =pickle.load(fileObj2)
            # item =pickle.load(open("item.txt","rb"), encoding="iso-8859-1")
            lyst2.append(item)
        except EOFError:
            fileObj2.close()
            break
    print(lyst2)



if __name__ == '__main__':
    main()