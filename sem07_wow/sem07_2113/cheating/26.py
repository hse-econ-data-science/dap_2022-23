n = int(input())
a = {}
for i in range(n):
    word = input()
    b = word.lower()
    if b not in a:
        a[b] = set()
    a[b].add(word)
errors = 0
s = input().split()
for word in s:
    b = word.lower()
    le = len([l for l in word if l.isupper()])
    if (b in a and word not in a[b] or le != 1):
        errors += 1
print(errors)