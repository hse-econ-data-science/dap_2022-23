L, K = list(map(int, input().split()))
N = list(map(int, input().split()))
a = N[0]
b = N[len(N) - 1]
for i in range(len(N)):
    if N[i] < L / 2:
        a = N[i]
for j in range(len(N) - 1, -1, -1):
    if N[j] >= L / 2:
        b = N[j]
if a == L // 2:
    print(a)
else:
    print(a)
    print(b)