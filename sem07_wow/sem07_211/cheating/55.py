L, K = map(int, input().split())
sr = (L - 1) / 2
s = list(map(int, input().split()))
i = 0
max1 = 0
while i < len(s) and s[i] < sr:
    max1 = s[i]
    i += 1
max2 = s[len(s) - 1]
i = len(s) - 1
while s[i] > sr:
    max2 = s[i]
    i -= 1
if (L - 1) % 2 == 0 and int((L - 1) / 2) in s:
    print(int((L - 1) / 2))
else:
    print(max1, max2)