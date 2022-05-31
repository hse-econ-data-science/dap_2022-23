n = int(input())
a = dict()
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in a:
        a[base_form] = set()
    a[base_form].add(word)
errors = 0
s = input().split()
for word in s:
    base_form = word.lower()
    if base_form in a and word not in a[base_form]:
        errors += 1
    elif len([l for l in word if l.isupper()]) != 1:
        errors += 1
print(errors)