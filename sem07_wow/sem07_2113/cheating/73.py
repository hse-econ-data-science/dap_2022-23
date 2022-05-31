x = list(map(int, input().split()))
n = x[0]
k = x[1]
lst = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append([[abs(lst[i] - k), lst[i]]])
for f in range(1, n):
    lst = list(map(int, input().split()))
    for j in range(n):
        arr[j].append([abs(lst[j] - k), lst[j]])
for i in range(n):
    arr[i].sort()
for i in range(n):
    for j in range(n - 1):
        print(arr[j][i][1], ' ', sep='', end='')
    print(arr[n - 1][i][1])