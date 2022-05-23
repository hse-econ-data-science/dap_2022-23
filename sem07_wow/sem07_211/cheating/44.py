t = input()
t1 = int(t[0])
t2 = int(t[1])
m1 = int(t[3])
m2 = int(t[4])
h = 10 * t1 + t2
if h <= 11:
    if h == 0:
        h += 12
    print(h, ':', m1, m2, ' a.m.', end='', sep='')
else:
    if h > 12:
        h -= 12
    print(h, ':', m1, m2, ' p.m.', end='', sep='')