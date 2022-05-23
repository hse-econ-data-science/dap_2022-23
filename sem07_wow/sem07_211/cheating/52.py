n = int(input())
s = ''
summ = 0
for i in range(1, n):
    s = s + str(i) + '*' + str(i + 1) + '+'
    summ = summ + i * (i + 1)
s = s[:-1]
print(s, summ, sep='=')