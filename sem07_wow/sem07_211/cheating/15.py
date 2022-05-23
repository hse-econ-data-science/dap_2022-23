yes = set(map(str, range(1, int(input()) + 1)))
for line in iter(input, 'HELP'):
    guesses = yes.intersection(line.split())
    if len(guesses) > (len(yes) - len(guesses)):
        print('YES')
        yes = guesses
    else:
        print('NO')
        yes -= guesses
print(*sorted(yes, key=int))