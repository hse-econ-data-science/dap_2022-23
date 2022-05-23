tot_cont = []
grade9 = []
grade10 = []
grade11 = []
tot_point = []
file = open('input.txt', 'r', encoding='utf-8')
for line in file:
    cont = list(line.split())
    tot_cont.append(cont)
tot_cont.sort(key=lambda x: int(x[2]))
max9 = 80
for i in tot_cont:
    if int(i[2]) == 9:
        grade9.append(i[3])
    elif int(i[2]) == 10:
        grade10.append(i[3])
    elif int(i[2]) == 11:
        grade11.append(i[3])
grade9.sort()
grade10.sort()
grade11.sort()
grade9 = grade9[::-1]
grade10 = grade10[::-1]
grade11 = grade11[::-1]
max9 = grade9[0]
max10 = grade10[0]
max11 = grade11[0]
kol9 = 0
kol10 = 0
kol11 = 0
for i in range(0, len(grade9)):
    if grade9[i] == max9:
        kol9 += 1
for i in range(0, len(grade10)):
    if grade10[i] == max10:
        kol10 += 1
for i in range(0, len(grade11)):
    if grade11[i] == max11:
        kol11 += 1
print(kol9, kol10, kol11)
