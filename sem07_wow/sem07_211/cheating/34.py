inp = open('input.txt', 'r', encoding='utf-8')
out = open('output.txt', 'w', encoding='utf-8')


def count_uppercase(s):
    count = 0
    for letter in s:
        if letter.isupper():
            count += 1
    return count


dict = set()
n = int(input())
for i in range(n):
    word = input()
    dict.add(word)
    dict.add(word.upper())
to_check = input().split()
count_mistakes = 0
for word in to_check:
    if word in dict and count_uppercase(word) == 1:
        continue
    if count_uppercase(word) == 1:
        if not word.upper() in dict:
            continue
    count_mistakes += 1
print(count_mistakes)