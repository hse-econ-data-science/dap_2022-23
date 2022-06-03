n = int(input())
k = set(i for i in range(1, n + 1))
while True:
    s = input()
    if s == "HELP":
        break
    s = set(map(int, s.split()))
    if len(k & s) > len(k) / 2:
        print("YES")
        k &= s
    else:
        print("NO")
        k -= s
print(*sorted(k))