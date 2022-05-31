inFile = open('input.txt', 'r', encoding='utf=8')
line_set = inFile.readlines()
temp = {}
for line in line_set:
    line = line.split()
    for word in line:
        temp[word] = temp.get(word, 0) + 1
subj = (temp.items())


def sort(a):
    for i in a:
        return -a[1], a[0]


for word in sorted(subj, key=sort):
    print(word[0])