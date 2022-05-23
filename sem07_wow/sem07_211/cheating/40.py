import sys


def A(inputsource, output):
    w = dict()
    for l in inputsource:
        for word in l.split():
            if word not in w:
                w[word] = 1
            else:
                w[word] += 1
    for i in sorted(w.items(), key=lambda x: (-x[1], x[0])):
        output.write(i[0] + '\n')
    return


def main():
    A(sys.stdin, sys.stdout)


main()