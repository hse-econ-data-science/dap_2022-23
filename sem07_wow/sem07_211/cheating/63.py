lst1 = input().split()
leng = int(lst1[0])
n = int(lst1[1])

x1 = 0
x2 = -1

data = []
data1 = input().split()
for i in range(n):
    data.append(int(data1[i]))
for i in range(n):
    if 2 * data[i] < leng:
        x1 = data[i]
    if (2 * data[i] + 2 > leng) and (x2 == -1):
        x2 = data[i]
if x1 == x2:
    print(x1)
else:
    print(x1, x2)