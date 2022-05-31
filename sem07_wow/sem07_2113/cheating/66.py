l, k = list(map(int, input().split()))
n = list(map(int, input().split()))
right = 0
left = 0
nearL = -1
nearR = l + 1
a = [0] * l
for i in range(len(n)):
    a[n[i]] = a[n[i]] + 1
if l % 2 == 0:
    nearL = l // 2 - 1
    nearR = l // 2
    for i in range(l):
        if i <= nearL and a[i] != 0:
            left = i
        if i >= nearR and right == 0 and a[i] != 0:
            right = i
    print(left, right)
else:
    near = l // 2
    if a[near] == 1:
        print(near)
    else:
        for i in range(l):
            if i < near and a[i] != 0:
                left = i
            if i > near and right == 0 and a[i] != 0:
                right = i
        print(left, right)