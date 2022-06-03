myList = list(map(int, input().split()))
count = 0
for i in range(1, len(myList) - 1):
    if myList[i] > myList[i - 1] and myList[i] > myList[i + 1]:
        count += 1
print(count)
