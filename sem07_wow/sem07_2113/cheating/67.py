l, k = map(int, input().split())
legs = list(map(int, input().split()))
middle = -1
legs_number = set()
legs_number1 = set()
for i in range(len(legs)):
    if (l - 1) / 2 == legs[i]:
        middle = legs[i]
    elif (l - 1) / 2 > legs[i]:
        legs_number.add(legs[i])
    elif (l - 1) / 2 < legs[i]:
        legs_number1.add(legs[i])
if middle != -1:
    print(middle)
else:
    print(max(legs_number), min(legs_number1))