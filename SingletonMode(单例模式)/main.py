from functools import wraps


# 继承实现単例---------------------------------------------------
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    a = 1


# --------------------------------------------------------------


# 装饰器实现単例--------------------------------------------------
def singleton(cls):
    instance = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return getinstance


@singleton
class TestClass(object):
    b = 1


# --------------------------------------------------------------

# metaclass(元类)------------------------------------------------
class Singleton2(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__()
        return cls._instances[cls]


class TestClass2(object):
    __metaclass__ = Singleton2
    b = 1


if __name__ == '__main__':
    one = MyClass()
    two = MyClass()
    oneT = TestClass()
    twoT = TestClass()
    bool1 = bool(one == two)
    bool2 = bool(oneT == twoT)
    id1 = (id(one), id(two))
    id2 = (id(oneT), id(twoT))
    print(bool1, id1)
    print(bool2, id2)
