l, k = map(int, input().split())
block = list(map(int, input().split()))
mid = -1
block_num1 = set()
block_num2 = set()
for i in range(len(block)):
    if (l - 1) / 2 == block[i]:
        mid = block[i]
    elif (l - 1) / 2 > block[i]:
        block_num1.add(block[i])
    elif (l - 1) / 2 < block[i]:
        block_num2.add(block[i])
if mid != -1:
    print(mid)
else:
    left = max(block_num1)
    right = min(block_num2)
    print(left, right)