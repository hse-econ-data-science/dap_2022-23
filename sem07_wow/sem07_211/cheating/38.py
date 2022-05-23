parties = list()
votes = list()
sumVotes = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        partyName = ' '.join(line[:-1])
        partyVotes = int(line[-1])
        parties.append(partyName)
        votes.append(partyVotes)
        sumVotes += partyVotes
mandates = list()
frac = []
sum_mandates = 0
for i in range(len(parties)):
    partyMandates = (votes[i] * 450) / sumVotes
    sum_mandates += int(partyMandates)
    mandates.append(int(partyMandates))
    frac.append(partyMandates - int(partyMandates))
while sum_mandates < 450:
    i = 0
    for j in range(1, len(frac)):
        if (frac[j] > frac[i]) or\
                (frac[j] == frac[i] and votes[j] > votes[i]):
            i = j
    mandates[i] += 1
    sum_mandates += 1
    frac[i] = 0

for k in range(len(parties)):
    print(parties[k], mandates[k])