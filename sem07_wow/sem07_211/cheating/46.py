x = int(input())
a = x // 100000 * 2
b = x // 10000 % 10
c = x // 1000 % 10 * 2
d = x % 1000 // 100
e = x % 100 // 10 * 2
f = x % 10
if a >= 9:
    a = a - 9
if c >= 9:
    c = c - 9
if e >= 9:
    e = e - 9
sum = a + b + c + d + e + f
if sum % 10 == 0:
    print('YES')
else:
    print('NO')