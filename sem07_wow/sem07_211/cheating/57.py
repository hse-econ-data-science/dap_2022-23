l, k = map(int, input().split())
a = list(map(int, input().split()))
p = 0
for i in range(len(a)):
    if l % 2 == 1 and k > 1 and a[i] != l // 2:
        p += 1
one = 0
two = 0
five = 0
first = []
sec = []
thrd = []
six = 0
forth = []
if k > 1 and l % 2 == 0:
    for i in range(len(a)):
        if a[i] < l // 2:
            one = one + 1
            first.append(a[i])
        else:
            two = two + 1
            thrd.append(a[i])
if one > 0 and two > 0:
    print(max(first), min(thrd))
if k > 1 and l % 2 == 1:
    for i in range(len(a)):
        if a[i] == l // 2:
            w = a[i]
            print(w)
if k > 1 and l % 2 == 1:
    for i in range(len(a)):
        if p == len(a):
            for i in range(len(a)):
                if a[i] < l // 2:
                    six = six + 1
                    sec.append(a[i])
                else:
                    five = five + 1
                    forth.append(a[i])
if six > 0 and five > 0:
    print(max(sec), min(forth))