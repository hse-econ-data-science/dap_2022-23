n = int(input())
sres = set(range(1, n + 1))
while True:
    cur = input()
    if cur == 'HELP':
        break
    cur = {int(x) for x in cur.split()}
    if len(sres & cur) > len(sres) / 2:
        print('YES')
        sres &= cur
    else:
        print('NO')
        sres -= cur
print(' '.join([str(x) for x in sorted(sres)]))