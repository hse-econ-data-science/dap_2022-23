l, n = map(int, input().split())
myl = list(map(int, input().split()))
a = myl[0]
b = myl[-1]
for i in range(n):
    if myl[i] < (l / 2):
        a = myl[i]

for i in sorted(myl, reverse=True):
    if i + 1 > (l / 2):
        b = i

if b == a and l % 2 == 1:
    print(b)
else:
    print(a, b)