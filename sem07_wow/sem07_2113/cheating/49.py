n = int(input())
l = list(map(int, input().split()))
res = []
am = n + 1
mx = 0
orl = []
for i in range(n):
    if (l[i] % 10 == 5):
        res.append((l[i], i))
    if (l[i] > mx):
        mx = l[i]
        mn = i
    elif (l[i] == mx):
        mn = min(mn, i)
mx = -1
for i in range(len(res)):
    if (res[i][1] == n - 1):
        continue
    if (l[res[i][1] + 1] >= res[i][0]):
        continue
    if (mn < res[i][1]):
        mx = max(mx, res[i][0])
if mx == -1:
    print(0)
else:
    mount = 0
    for i in range(n):
        if l[i] > mx:
            mount += 1
    print(mount + 1)