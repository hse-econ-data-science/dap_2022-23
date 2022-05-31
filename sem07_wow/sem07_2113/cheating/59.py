n, m = map(int, input().split())
a = list(map(int, input().split()))
b = 0
for i in range(len(a)):
    if n % 2 == 1 and m > 1 and a[i] != n // 2:
        b = b + 1
s = 0
d = 0
q = 0
v = 0
g = 0
l = []
f = []
p = []
d = 0
h = 0
x = []
if m > 1 and n % 2 == 0:
    for i in range(len(a)):
        if a[i] < n // 2:
            s = s + 1
            l.append(a[i])
        else:
            d = d + 1
            p.append(a[i])
if s > 0 and d > 0:
    print(max(l), min(p))
if m > 1 and n % 2 == 1:
    for i in range(len(a)):
        if a[i] == n // 2:
            w = a[i]
            print(w)
if m > 1 and n % 2 == 1:
    for i in range(len(a)):
        if b == len(a):
            for i in range(len(a)):
                if a[i] < n // 2:
                    h = h + 1
                    f.append(a[i])
                else:
                    g = g + 1
                    x.append(a[i])
if h > 0 and g > 0:
    print(max(f), min(x))