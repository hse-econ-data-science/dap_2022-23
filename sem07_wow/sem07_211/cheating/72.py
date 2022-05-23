n, k = map(int, input().split())
a = []
s = list(map(int, input().split()))
for i in range(n):
    a.append([[abs(s[i]-k), s[i]]])
for i in range(1, n):
    s = list(map(int, input().split()))
    for j in range(n):
        a[j].append([abs(s[j]-k), s[j]])

for i in range(n):
    a[i].sort()

for i in range(n):
    for j in range(n-1):
        print(a[j][i][1], ' ', sep='', end='')
    print(a[n-1][i][1])