class Student(object):
    __slots__ = ('name', 'gender', 'age')

    def __init__(self, name, gender, age):
        self.name = name,
        self.gender = gender,
        self.age = age,


if __name__ == '__main__':
    man = Student('horsun', 'male', '23')
    print(man)
    man.height = '188'
# Traceback (most recent call last):
#   File "/home/horsun/Desktop/self-learn/__slots__/main.py", line 13, in <module>
#     man.height = '188'
# AttributeError: 'Student' object has no attribute 'height'
