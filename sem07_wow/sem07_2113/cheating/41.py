import sys


def Solving(inputsource, output):
    words = dict()
    for line in inputsource:
        for word in line.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    for i in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        output.write(i[0] + '\n')
    return


def main():
    Solving(sys.stdin, sys.stdout)


main()