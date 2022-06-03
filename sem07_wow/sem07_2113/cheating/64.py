dt = input().split()
length = int(dt[0])
n = int(dt[1])


ans1 = 0
ans2 = -1


data = []

data_ = input().split()


for i in range(n):
    data.append(int(data_[i]))

for i in range(n):
    if 2 * data[i] < length:
        ans1 = data[i]
    if 2 * data[i] + 2 > length and ans2 == -1:
        ans2 = data[i]

if ans1 == ans2:
    print(ans1)
else:
    print(ans1, ans2)