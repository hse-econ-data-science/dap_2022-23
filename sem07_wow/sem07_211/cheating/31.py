n = int(input())
acnts = {}
for i in range(n):
    word = input()
    base_frm = word.lower()
    if base_frm not in acnts:
        acnts[base_frm] = set()
    acnts[base_frm].add(word)

errors = 0
sent = input().split()
for word in sent:
    base_frm = word.lower()
    if (not (not (base_frm in acnts and word not in acnts[base_frm]) and not (
            len([l for l in word if l.isupper()]) != 1))):
        errors += 1
print(errors)