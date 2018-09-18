"""
简单搜索算法
"""
def indexOfMin(lyst):
    """返回数组中最小项的索引"""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex


def sequentialSearch(target,lyst):
    """搜索数组中某一项的索引"""
    position = 0
    while position <len(lyst):
        if target ==lyst[position]:
            return position
        position += 1
    return -1

def binarySearch(target, sortedLyst):
    """二叉搜索(二分查找)
        必须是有序列表 必须是同种类型
        列表长度 = n
        最多执行次数： n/2/2/2... 即 n/(2**k)
        求最大次数k： n=2**k     k = log2(n)
        复杂度：O(log2(n))

        例如n=1000000  k=20  2**20>1000000
        明显优于顺序搜索的k=1000000次
    """
    left = 0
    right = len(sortedLyst) - 1
    while left < right:
        midPoint = (left + right) // 2  # 取整
        if target == midPoint:
            return midPoint
        elif target < midPoint:
            right = midPoint - 1
        else:
            left = midPoint + 1
    return -1


print(2**20)