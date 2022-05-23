def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        i = 2
        b = a
        while i <= n:
            a = a * b
            i += 1
        return a
    else:
        i = 0
        b = a
        a = 1
        while i > n:
            a = a / b
            i -= 1
        return a


a = float(input())
n = int(input())
print(power(a, n))
