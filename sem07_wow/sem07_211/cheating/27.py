n = int(input())
a = {}
for i in range(n):
    word = input()
    base = word.lower()
    if base not in a:
        a[base] = set()
    a[base].add(word)

mistakes = 0
sent = input().split()
for word in sent:
    base = word.lower()
    if base in a and word not in a[base]:
        mistakes += 1
    elif len([l for l in word if l.isupper()]) != 1:
        mistakes += 1
print(mistakes)