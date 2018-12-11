import asyncio
import threading
import time


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = yield from asyncio.sleep(5)
    print('Hello world! (%s)' % threading.currentThread())


@asyncio.coroutine
def job(t):
    print("Start job", t)
    r = yield from asyncio.sleep(t)
    print("Job", t, 'takes', t, 's')


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    # task = [hello(), hello()]
    task = [job(1), job(2)]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()
    print("Async total time : ", time.time() - t1)

