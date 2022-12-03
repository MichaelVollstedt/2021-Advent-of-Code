#fileName = '06_advent_test.txt'
fileName = '06_advent.txt'
lanternFishes = []

def readFile():
    global lanternFishes

    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip().split(',')
        mapping = map(int, line)
        line = list(mapping)
        lanternFishes = line

def updateLanterFish(lanternFishes):

    i = 0
    existingFishes = len(lanternFishes)
    while i < existingFishes:
        if lanternFishes[i] == 0:
            lanternFishes[i] = 6
            lanternFishes.append(int(8))

        elif lanternFishes[i] > 0:
            lanternFishes[i] -= 1

        i += 1

def checkOverdueFish(fish):
    if fish < 0:
        return fish + 7
    else:
        return fish

def makeNewFish(n):
    newFishes = [8] * n
    return newFishes

def reduceFishTimer(fish):
    #fish -= 1
    return fish - 1

def updateLanterFishFaster(lanternFishes):
    #reduce all fishes by one and count overdue fishes, after that we reset counter and add new fishes
    reduced = []

    countNewFish = lanternFishes.count(0)
    reduced.extend(list(map(lambda x: x - 1 if x != 0 else 6, lanternFishes)))

    if countNewFish > 0:
        reduced.extend(makeNewFish(countNewFish))
    lanternFishes.clear()
    lanternFishes.extend(reduced)

def updateLanterFishLifes(fishes):
    days = [0] * 9
    # Update the current numbers
    for fish in fishes:
        days[fish] += 1
    for i in range(256):
        # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
        today = i % len(days)
        # Add new babies
        days[(today + 7) % len(days)] += days[today]
    print(f'Total lanternfish after 256 days: {sum(days)}')

if __name__ == '__main__':
    readFile()
    updateLanterFishLifes(lanternFishes)
    #i = 1
    #timer = 256
    #while i <= timer:
    #    print('Current Day = ' + str(i))
    #    updateLanterFishFaster(lanternFishes)
    #    i += 1
    #print(lanternFishes)
    #print('Count of fishes after 80 days = ' + str(len(lanternFishes)))