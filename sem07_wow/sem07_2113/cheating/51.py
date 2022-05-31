n = int(input())
s = ''
suma = 0
for i in range(1, n):
    s = s + str(i) + '*' + str(i + 1) + '+'
    suma = suma + i * (i + 1)
s = s[:-1]
print(s, suma, sep='=')