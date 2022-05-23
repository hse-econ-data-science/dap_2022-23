s = input()
h1 = int(s[0])
h2 = int(s[1])
h = 10 * h1 + h2

m1 = int(s[3])
m2 = int(s[4])
m = 10 * m1 + m2
if 11 >= h >= 0:
    if h == 0:
        h += 12
    print(h, ':',  m1, m2, ' a.m.',  end='', sep='')
else:
    if h > 12:
        h -= 12
    print(h, ':', m1, m2, ' p.m.', end='', sep='')