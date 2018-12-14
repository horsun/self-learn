def grep(pattern):
    """

    :param pattern:
    :return:
    """
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


def xrange(n):
    """
    生成器
    :param n:
    :return:
    """
    while True:
        if n > 0:
            n -= 1
            yield n
        else:
            break


if __name__ == '__main__':
    search = grep('apple')
    next(search)
    search.send('here is a peach')
    search.send('here is a melon')
    search.send('here is a apple')
