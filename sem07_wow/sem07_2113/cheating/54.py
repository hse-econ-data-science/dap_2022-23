N, K = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(N):
        if i < j:
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
for i in range(N):
    mat[i] = sorted(mat[i], key=lambda X: [abs(X - K), X])
for i in range(N):
    for j in range(N):
        if i < j:
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
for i in range(N):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()