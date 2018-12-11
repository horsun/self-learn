def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


if __name__ == '__main__':
    search = grep('apple')
    next(search)
    search.send('here is a peach')
    search.send('here is a melon')
    search.send('here is a apple')
