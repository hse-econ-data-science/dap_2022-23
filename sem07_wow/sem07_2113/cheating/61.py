a, b = map(int, input().split())
k = [int(i) for i in input().split()]
left = k[0]
right = k[-1]
for i in range(b):
    if k[i] < (a / 2):
        left = k[i]

for i in sorted(k, reverse=True):
    if i + 1 > (a / 2):
        right = i

if right == left and a % 2 == 1:
    print(right)
else:
    print(left, right)