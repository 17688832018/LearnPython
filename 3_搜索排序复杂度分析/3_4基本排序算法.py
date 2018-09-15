"""
选择排序 冒泡排序 插入排序等
"""
def swap(lyst,i,j):
    """交换列表中某两项的位置"""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    """选择排序：搜索列表，将最小项放到第一个位置，在剩余的列表里继续搜索最小项放到第二个位置
        总次数为：(n-1)+(n-2)+(n-3)+...+1 = n(n-1)/2 = 1/2 * n**2 - 1/2 * n
        复杂度为：O(n**2)
    """
    # lyst= [5,3,1,2,4]
    i = 0
    while i<len(lyst)-1:  # 共n轮(索引从0-4,5个位置)
        minIndex = i
        j = i+1
        while j <len(lyst):  # 每轮搜n-j次 (第2、3、4、5个位置与第一个位置比出最小的)
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:  # 最小的若不在该轮的正确位置上
            swap(lyst,minIndex,i)
        i += 1


def bubbleSort(lyst):
    """冒泡排序
        总次数：1/2 * n(n-1)
        复杂度：O(n**2) 与选择排序相同
        优化了最优情况，平均和最差情况时复杂度不变
    """
    for i in range(len(lyst)):
        swaped = False
        for j in range(len(lyst)-1):
            if lyst[j] > lyst[j+1]:
                swap(lyst,j,j+1)
                swaped = True
        if not swaped:
            return lyst


list1 = [5,9,7,4,2,10,8,1,3,6]
print(bubbleSort(list1))