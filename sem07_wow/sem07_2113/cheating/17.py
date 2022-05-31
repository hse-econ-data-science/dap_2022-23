k = int(input())
n = set(i for i in range(1, k + 1))
while True:
    s = input()
    if s == "HELP":
        break
    s = set(map(int, s.split()))
    if len(n & s) > len(n) / 2:
        print("YES")
        n &= s
    else:
        print("NO")
        n -= s
print(*sorted(n))