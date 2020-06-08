import cv2
#python实现冒泡排序
def bubble_sort(nums):    #时间复杂度为O(n*2)
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#python实现选择排序算法
def select_sort(items):
    """
    选择排序，简单而直观，其原理是把序列中的最小值或者最大值找出来放在起始位置，
    然后再从剩下的序列中找出极值放到起始位置之后，以此类推最后就完成排序.
    选择排序的交换操作介于 0 和 (n - 1） 次之间。选择排序的比较操作为 n (n - 1） / 2 次之间。选择排序的赋值操作介于 0 和 3 (n - 1） 次之间。
    比较次数O(n^2），比较次数与关键字的初始状态无关，总的比较次数N=(n-1）+(n-2）+...+1=n*(n-1）/2。交换次数O(n），最好情况是，已经有序，交换0次；最坏情况交换n-1次，逆序交换n/2次。交换次数比冒泡排序少多了，由于交换所需CPU时间比比较所需的CPU时间多，n值较小时，选择排序比冒泡排序快。
    :param items:
    :return:
    """

    n = len(items)
    for cur in range(n-1):
        item_max = cur
        for i in range(cur+1, n):
            if items[i] > items[item_max]:
                items[i], items[item_max] = items[item_max], items[i]
        if item_max != cur:
           items[cur], items[item_max] = items[item_max], items[cur]

#python实现插入排序算法
def insert_sort(items):
    """
    插入排序，其原理是通过构建一个初始的有序序列，然后从无需序列中抽取元素，插入到有序序列的相对排序位置，就像将一堆编号混乱的书，一本一本的放到书架上，找到上下编号之间的位置插入，最后完成整理。
    :param items:
    :return:
    """




    # for i in range(1, len(items)):
image = cv2.imread("G:\\pic2020\\2\\circle_1 (801).jpg",0)
dstvar = cv2.Laplacian(image, cv2.CV_64F).var()
print(dstvar)