def transpose(matrix, n):
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] =\
                    matrix[j][i], matrix[i][j]


n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
transpose(matrix, n)
for i in range(n):
    matrix[i] = sorted(matrix[i], key=lambda x: [abs(x - k), x])
transpose(matrix, n)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()