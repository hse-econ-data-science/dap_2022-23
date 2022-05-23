inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
counter = {}
for line in lines:
    line = line.split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
items = (counter.items())


def sorter(a):
    for number in a:
        return -a[1], a[0]


for word in sorted(items, key=sorter):
    print(word[0])