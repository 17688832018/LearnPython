"""搜索算法习题"""
# 二叉搜索
def searchList(target,list):
    leftIndex = 0
    rightIndex = len(list)-1
    while list[leftIndex]<list[rightIndex]:
        midIndex = (leftIndex+rightIndex)//2  # midIndex是动态变化的
        result = "left=%d,right=%d,mid=%d" % (list[leftIndex], list[rightIndex], list[midIndex])
        if target == list[midIndex]:
            return " successful!%s" % result
        elif target < list[midIndex]:
            rightIndex = midIndex-1
            print(result)
        else:
            leftIndex = midIndex+1
            print(result)
    return -1

list1 =[20,44,48,55,62,66,74,88,93,99]
# obj1 = searchList(90,list1)
# 方法里有print时，调用时传参即可有输出
obj2 = searchList(44,list1)
# print(obj1)
print(obj2)

# 三叉搜索
def searchList3(target,list):
    leftIndex = 0
    rightIndex = len(list) -1
    while list[leftIndex] < list[rightIndex]:
        index1 = (leftIndex + rightIndex) //3
        index2 = (leftIndex + rightIndex) //3 *2
        print("0-",list[index1],list[index2])
        result = "left=%d,right=%d,index1=%d,index2=%d" % (list[leftIndex], list[rightIndex], index1,index2)
        if target == list[index1] or target == list[index2]:
            return "successful! %s" % result
        if target <list[index1]:
            rightIndex = index1-1
            print("1-",result)
        elif target > list[index2]:
            leftIndex = index2 + 1
            print("2-",result)
        else:
            print(leftIndex,rightIndex)
            print("3-", result)
            leftIndex = index1+1
            rightIndex = index2-1
            print(leftIndex, rightIndex)
            print("4-",result)
    return -1


list2 = []
for i in range(0,30,2):
    list2.append(i)
print(list2)
obj3 = searchList3(26,list2)
print(obj3)