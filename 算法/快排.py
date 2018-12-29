import time


def timeFilter(func):
    def swage(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        print(f"it's takes {time.time() - t1} seconds")

    return swage


# @timeFilter
def quickSort(arr):
    less = []  # 比 基准小的
    pivotList = []  # 相等的list
    more = []  # 比基准大的
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 将第一个值做为基准
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)  # 得到第一轮分组之后，继续将分组进行下去。
        more = quickSort(more)

        return less + pivotList + more


if __name__ == '__main__':
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(quickSort(a))
