import math


def rev():
    n = int(input())
    if n != 0:
        rev()
        if (math.sqrt(n).is_integer()):
            global flag
            flag = 1
            print(n)

flag = 0
rev()
if flag == 0:
    print(0)
