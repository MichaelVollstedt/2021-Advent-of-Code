
fileName = '11_advent.txt'
energyLevel = []
flashCounter = 0

def readFile(energyLevel):
    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip()
        energyLevel.append(line)

    for i, x in enumerate(energyLevel):
        energyLevel[i] = [int(char) for char in x]

def updateEnergyLevel():
    global energyLevel

    for i, line in enumerate(energyLevel):
        new_line = [x + 1 for x in line]
        energyLevel[i] = new_line

def octopusFlashes():
    global flashCounter

    for l, line in enumerate(energyLevel):
        for i, octo in enumerate(line):
            if octo > 9:
                line[i] = -1000000
                flashCounter += 1
                updatedAdjacentOctopus(l, i, line)

def checkBorders(line, pos):
    check = False
    lineLength = len(line)
    listLength = len(energyLevel)

    if pos-1 >= 0 and pos+1 < lineLength and line-1 >= 0 and line + 1 < listLength:
        check = True

def updatedAdjacentOctopus(i_line, pos, line):
    global energyLevel
    lineLength = len(line)
    listLength = len(energyLevel)

    if pos-1 >= 0:
        energyLevel[i_line][pos - 1] += 1
    if pos+1 < lineLength:
        energyLevel[i_line][pos + 1] += 1
    if i_line - 1 >= 0:
        energyLevel[i_line - 1][pos] += 1
    if i_line + 1 < listLength:
        energyLevel[i_line + 1][pos] += 1
    if i_line - 1 >= 0 and pos - 1 >= 0:
        energyLevel[i_line - 1][pos - 1] += 1
    if i_line - 1 >= 0 and pos + 1 < lineLength:
        energyLevel[i_line - 1][pos + 1] += 1
    if i_line + 1 < listLength and pos - 1 >= 0:
        energyLevel[i_line + 1][pos - 1] += 1
    if i_line + 1 < listLength and pos + 1 < lineLength:
        energyLevel[i_line + 1][pos + 1] += 1

def checkForGreaterNines():
    check = False
    for line in energyLevel:
        line2 = [i for i in line if i > 9]
        if len(line2) > 0:
            check = True
            break

    return check

def checkSynchronizedFlash():
    check = True
    for line in energyLevel:
        checkLine = all(i < 0 for i in line)
        if checkLine:
            check = False
        else:
            check = True
            break
    return check

def resetOctopus():
    for line in energyLevel:
        for i, octo in enumerate(line):
            if octo < 0:
                line[i] = 0

if __name__ == '__main__':
    readFile(energyLevel)
    print(energyLevel)
    i = 0
    while checkSynchronizedFlash():
        resetOctopus()
        print('Step = ' + str(i))
        updateEnergyLevel()
        while checkForGreaterNines():
            octopusFlashes()
        i += 1

    print(flashCounter)
    print(energyLevel)
    print('Number of Steps = ' + str(i))