import statistics
import numpy
from collections import Counter

#fileName = '07_advent_test.txt'
fileName = '07_advent.txt'
crabs = []


def readFile():
    global crabs

    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip().split(',')
        mapping = map(int, line)
        line = list(mapping)
        crabs = line

def findBestStartingPosition(sortedCrabs):

    crabPositions = Counter(sortedCrabs)
    print('Crab Positions Aggregated: \n' + str(crabPositions))

    startCrab = list(crabPositions.keys())[0]
    endCrab = list(crabPositions.keys())[-1]
    length = endCrab - startCrab + 1
    fuelConsumption = [0] * length

    i = 0
    while i < length:
        # for every crab position find fuel consumption

        fuel = 0
        fuelNew = 0
        for crab in crabPositions:
            #print('Key = ' + str(crab) + ' Value = ' + str(crabPositions[crab]))
            distance = abs(startCrab - crab)
            fuel += distance * crabPositions[crab]
            fuelNew += sum(range(distance+1)) * crabPositions[crab]

        fuelConsumption[i] = fuelNew
        startCrab += 1
        i += 1

    return fuelConsumption



def analytics(crabs):
    print(crabs)

    f = statistics.mean(crabs)
    print('Mean = ' + str(f))

    x = numpy.std(crabs)
    print('standard deviation = ' + str(x))

    y = numpy.var(crabs)
    print('variance = ' + str(y))

if __name__ == '__main__':
    readFile()
    crabs.sort()
    fuelConsumption = findBestStartingPosition(crabs)
    fuelConsumption.sort()
    print('Fuel Consumption List: \n ' + str(fuelConsumption))
    print('Most Efficient FuelConsumption: \n' + str(fuelConsumption[0]))

