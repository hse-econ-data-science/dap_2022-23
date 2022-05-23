n = int(input())
s = ''
summa = 0
for i in range(1, n):
    s = s + str(i) + '*' + str(i + 1) + '+'
    summa = summa + i * (i + 1)
s = s[:-1]
print(s, summa, sep='=')