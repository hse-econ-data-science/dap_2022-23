l, k = map(int, input().split())
m = (l - 1) / 2
s = [int(x) for x in input().split()]
i = 0
max1 = 0
while i < len(s) and s[i] < m:
    max1 = s[i]
    i += 1
max2 = s[len(s) - 1]
i = len(s) - 1
while s[i] > m:
    max2 = s[i]
    i -= 1
if (l - 1) % 2 == 0 and int((l - 1) / 2) in s:
    print(int((l - 1) / 2))
else:
    print(max1, max2)