n = int(input())
a = {}
for i in range(n):
    word = input()
    b = word.lower()
    if b not in a:
        a[b] = set()
    a[b].add(word)

err = 0
sent = input().split()
for word in sent:
    b = word.lower()
    if b in a and word not in a[b] \
            or len([l for l in word if l.isupper()]) != 1:
        err += 1
print(err)