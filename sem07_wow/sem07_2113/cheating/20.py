n = int(input())
a = set(range(1, n + 1))
b = a
while True:
    c = input()
    if c == 'HELP':
        break
    c = {int(x) for x in c.split()}
    if len(b & c) > len(b) / 2:
        print('YES')
        b &= c
    else:
        print('NO')
        b -= c

print(' '.join([str(x) for x in sorted(b)]))