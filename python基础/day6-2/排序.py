list = [2, 8, 1, 3 , 11, 58, 6 ,88 ,4 ,6, 10]
#冒泡排序 时间复杂度O（n**2）
# def bubble(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-1-i):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list
# print(bubble(list))

#选择排序
# def choose(list):
#     for i in range(len(list)-1):
#         min = i
#         for j in range(i+1, len(list)):
#             if list[j] < list[min]:
#                 min = j
#         if min != i:
#             list[i], list[min] = list[min], list[i]
#     return list
# print(choose(list))

#插入排序
def insert(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list
# print(insert(list))

#快速排序
def quick_sort(list, start, end):
    if start >= end:
        return
    mid = list[start]
    low = start
    high = end
    while low < high:
        while low < high and list[high] >= mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < mid:
            low += 1
        list[high] = list[low]

    list[low] = mid
    quick_sort(list, start, low-1)
    quick_sort(list, low+1, end)
# quick_sort(list, 0, len(list)-1)
# print(list)
def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist)//2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left,right)

def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = merge_sort(alist)
print(sorted_alist)
print(merge([1,3,2],[2,5,4]))