import itertools


# 无限迭代
def unLimit():
    num = itertools.count()
    for i in num:
        if i > 9999:
            break
        print(i)


# 指定值和步长
def withLimit():
    num = itertools.count(0, 2)
    for i in num:
        if i > 9999:
            break
        print(i)


# 对指定string进行迭代
def withLimitString(limit_string):
    stringIter = itertools.cycle(limit_string)
    i = 0
    for item in stringIter:
        if i >= 5:
            break
        print(item)
        i += 1


# 对指定string进行整体迭代
def withTotalString(total_string):
    stringIter = itertools.repeat(total_string, 3)
    print(type(stringIter))
    print(list(stringIter))



if __name__ == '__main__':
    # withLimit()
    # withLimitString('apple')
    withTotalString('apple')
