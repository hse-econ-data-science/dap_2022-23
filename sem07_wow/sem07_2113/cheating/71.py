n, k = map(int, input().split())
mas = []
s = list(map(int, input().split()))
for i in range(n):
    mas.append([[abs(s[i]-k), s[i]]])
for f in range(1, n):
    s = list(map(int, input().split()))
    for j in range(n):
        mas[j].append([abs(s[j]-k), s[j]])

for e in range(n):
    mas[e].sort()

for i in range(n):
    for j in range(n-1):
        print(mas[j][i][1], ' ', sep='', end='')
    print(mas[n-1][i][1])