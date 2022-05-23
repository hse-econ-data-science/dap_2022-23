P_23, D_23 = list(map(int, input().split()))
n_23 = list(map(int, input().split()))
x_23 = n_23[0]
y_23 = n_23[len(n_23) - 1]
for k in range(len(n_23)):
    if n_23[k] < P_23 / 2:
        x_23 = n_23[k]
for i in range(len(n_23) - 1, -1, -1):
    if n_23[i] >= P_23 / 2:
        y_23 = n_23[i]
if x_23 == P_23 // 2:
    print(x_23)
else:
    print(x_23)
    print(y_23)