l, k = map(int, input().split())
blok = list(map(int, input().split()))
a = [0] * l
k1 = k2 = 0
for i in range(len(blok)):
    a[blok[i]] += 1
if l % 2 == 0:
    g1 = l // 2 - 1
    g2 = l // 2
    for i in range(len(a)):
        if a[i] != 0 and i <= g1:
            k1 = i
        if a[i] != 0 and i >= g2 and k2 == 0:
            k2 = i
    print(k1, k2)
else:
    g = l // 2
    if a[g] == 1:
        print(g)
    else:
        for i in range(len(a)):
            if a[i] != 0 and i < g:
                k1 = i
            if a[i] != 0 and i > g and k2 == 0:
                k2 = i
        print(k1, k2)