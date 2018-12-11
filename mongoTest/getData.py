import time

import psutil

_ONE_GIGABYTES_ = 1073741824


def sys_io_info():
    base_data = psutil.virtual_memory()
    data = {}
    data['total'] = base_data.total / _ONE_GIGABYTES_
    data['available'] = base_data.available / _ONE_GIGABYTES_
    data['percent'] = base_data.percent
    data['used'] = base_data.used / _ONE_GIGABYTES_
    data['cpu'] = psutil.cpu_percent(interval=0, percpu=True)

    return data


if __name__ == '__main__':
    time.sleep(1)
    print(sys_io_info())
