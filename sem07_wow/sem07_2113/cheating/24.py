n = int(input())
accents = {}
for i in range(n):
    word = input()
    form = word.lower()
    if form not in accents:
        accents[form] = set()
    accents[form].add(word)
mistakes = 0
line = input().strip().split()
for word in line:
    form = word.lower()
    if form in accents and word not in accents[form] or \
            len([elem for elem in word if elem.isupper()]) != 1:
        mistakes += 1
print(mistakes)