import socket

import gevent


def test1():
    print("12")
    gevent.sleep(3)
    print("34")


def test2():
    print("56")

    gevent.sleep(1)
    print("78")


def crawl():
    urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=5)

    print([job.value
           for job in jobs])


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),
    ])
    crawl()
