import math

fileName = '10_advent.txt'
navigation = []
openChar = ['[', '(', '{', '<']
closeChar = [']', ')', '}', '>']
points = [ 57, 3, 1197, 25137]
points2 = [ 2, 1, 3, 4]


def readFile(navigation):
    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip()
        navigation.append(line)

if __name__ == '__main__':
    readFile(navigation)
    print(navigation)

    total = 0
    countCorrupted = 0
    stack = []
    pointsToClose = 0
    pointsTotal = []

    for line in navigation:
        corrupted = False

        for char in line:
            if char in openChar:
                stack.append(char)
            elif char in closeChar:
                index = closeChar.index(char)
                if stack[-1] != openChar[index]:
                    total += points[index]
                    countCorrupted += 1
                    corrupted = True
                    break
                else:
                    del(stack[-1])

        if not corrupted:
            for char in reversed(stack):
                index = openChar.index(char)
                pointsToClose = pointsToClose * 5
                pointsToClose += points2[index]
            pointsTotal.append(pointsToClose)
            pointsToClose = 0
        stack = []

    print('Total Corrupted = ' + str(countCorrupted))
    print('Total Points For Corrupted = ' + str(total))

    pointsTotal.sort()
    print('Länge = ' + str(len(pointsTotal)))
    middle = len(pointsTotal) / 2
    middle = math.floor(middle)
    print('Mitte = ' + str(middle))
    print('Closing Point for Not Corrupted Lines \n ' + str(pointsTotal))
    print('Winning Points in Middle \n ' + str(pointsTotal[middle]))


