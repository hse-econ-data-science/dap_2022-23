infile = open('input.txt', 'r', encoding='utf-8')
oufile = open('output.txt', 'w', encoding='utf-8')


def count_upper(s):
    count = 0
    for letter in s:
        if letter.isupper():
            count += 1
    return count


dict = set()
n = int(input())
for i in range(n):
    slovo = str(input())
    dict.add(slovo)
    dict.add(slovo.upper())
check = input().split()
mistakes = 0
for slovo in check:
    if slovo in dict and count_upper(slovo) == 1:
        continue
    if count_upper(slovo) == 1:
        if not slovo.upper() in dict:
            continue
    mistakes += 1
print(mistakes)
# finally)) 0:40 a.m.