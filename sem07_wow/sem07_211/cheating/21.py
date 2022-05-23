n = int(input())
pn = set(range(1, n + 1))
while True:
    g = input()
    if g == 'HELP':
        break
    g = {int(x) for x in g.split()}
    if len(pn & g) > len(pn) / 2:
        print('YES')
        pn &= g
    else:
        pn -= g
        print('NO')
print(' '.join([str(x) for x in sorted(pn)]))