m, n = map(int, input().split())
blocks = list(map(int, input().split()))
less = blocks[0]
more = blocks[-1]
k = 0
for i in range(n):
    if blocks[i] < (m / 2):
        less = blocks[i]

for i in sorted(blocks, reverse=True):
    if i + 1 > (m / 2):
        more = i

if more == less and m % 2 == 1:
    print(more)
else:
    print(less, more)