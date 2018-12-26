from bisect import *


def binarySearch(lst, value, low, high):
    # low,high是lst的查找范围
    if high < low:
        return -1
    mid = (low + high) / 2
    if lst[mid] > value:
        return binarySearch(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binarySearch(lst, value, mid + 1, high)
    else:
        return mid


# 也可以不用递归方法，而采用循环，如下：

def bsearch(l, value):
    lo, hi = 0, len(l) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


def bisectSearch(lst, x):
    # bisect_left(lst,x)得到x在已经排序的lst中的位置
    i = bisect_left(lst, x)
    if i != len(lst) and lst[i] == x:
        return i


if __name__ == "__main__":
    lst = sorted([2, 5, 3, 8])
    print(bisectSearch(lst, 5))
    print(bsearch(lst, 5))
