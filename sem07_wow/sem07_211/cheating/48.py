n = int(input())
a = list(map(int, input().split()))
ans = []
mun = n + 1
mux = 0
top = []
for i in range(n):
    if (a[i] % 10 == 5):
        ans.append((a[i], i))
    if (a[i] > mux):
        mux = a[i]
        muni = i
    elif (a[i] == mux):
        muni = min(muni, i)
mux = -1
for i in range(len(ans)):
    if (ans[i][1] == n - 1):
        continue
    if (a[ans[i][1] + 1] >= ans[i][0]):
        continue
    if (muni < ans[i][1]):
        mux = max(mux, ans[i][0])
if (mux == -1):
    print(0)
else:
    kol = 0
    for i in range(n):
        if (a[i] > mux):
            kol += 1
    print(kol + 1)