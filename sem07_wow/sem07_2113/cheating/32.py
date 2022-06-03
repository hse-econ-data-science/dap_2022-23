n = int(input())
accents = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)

errors = 0
sent = input().split()
for word in sent:
    base_form = word.lower()
    if base_form in accents and word not in accents[base_form] \
            or len([l for l in word if l.isupper()]) != 1:
        errors += 1
print(errors)