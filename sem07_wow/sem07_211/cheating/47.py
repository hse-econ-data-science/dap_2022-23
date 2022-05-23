n = int(input())
a = n // 100000 * 2
b = n // 10000 % 10
c = n // 1000 % 10 * 2
d = n % 1000 // 100
e = n % 100 // 10 * 2
f = n % 10
if (a >= 9):
    a = a - 9
if (c >= 9):
    c = c - 9
if (e >= 9):
    e = e - 9
sum = a + b + c + d + e + f
if (sum % 10 == 0):
    print('YES')
else:
    print('NO')