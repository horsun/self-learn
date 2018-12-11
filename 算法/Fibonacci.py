import time


def Fibonacci(n):
    a = 0
    b = 1
    for item in range(n):
        a, b = b, a + b
    return a


def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))


if __name__ == '__main__':
    n = 2
    now = time.time()
    print(Fibonacci(n))
    print('coast:%s s' % (time.time() - now))
    now_2 = time.time()
    print(Fibonacci_Yield(n))
    print('coast:%s s' % (time.time() - now_2))
