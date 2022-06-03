names = list()
votes = list()
sumVotes = 0
inFile = open('input.txt')
for line in inFile:
    line = line.split()
    partyName = ' '.join(line[:-1])
    partyVotes = int(line[-1])
    names.append(partyName)
    votes.append(partyVotes)
    sumVotes += partyVotes
inFile.close()

mandates = list()
fracPart = []
sumMandates = 0
for i in range(len(names)):
    partyMandates = (votes[i] * 450) / sumVotes
    sumMandates += int(partyMandates)
    mandates.append(int(partyMandates))
    fracPart.append(partyMandates - int(partyMandates))

while sumMandates < 450:
    i = 0
    for j in range(1, len(fracPart)):
        if (
                (fracPart[j] > fracPart[i]) or
                (fracPart[j] == fracPart[i] and votes[j] > votes[i])
        ):
            i = j
    mandates[i] += 1
    sumMandates += 1
    fracPart[i] = 0

for k in range(len(names)):
    print(names[k], mandates[k])