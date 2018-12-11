import math

target = input("请输入一个数字:")
while True:
    try:
        target = int(target)
        break
    except ValueError:
        target = input("请输入一个数字！！:")
mystr = []
time = 0
while True:
    if target == 0:
        break
    log = int(math.log(target, 2))
    target = target - 2 ** log
    time += 1
    if not mystr:
        for i in range(log + 1):
            mystr.append('0')
        mystr[log] = '1'
    else:
        mystr[log] = '1'
mystr.reverse()
mystr = ''.join(mystr)
print(mystr)
