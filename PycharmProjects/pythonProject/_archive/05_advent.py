import numpy as np
fileName = '05_advent.txt'
rawListOfCoordinates = []
listOfCoordinates = []
vents = np.zeros((1000,1000), dtype=int)

def readFile():
    global listOfCoordinates
    global rawListOfCoordinates

    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        rawListOfCoordinates.append(line)
        line = line.strip().split(' -> ')
        line = [d.strip().split(",") for d in line]
        line = [list(map(int, d)) for d in line]
        listOfCoordinates.append(line)

    print(listOfCoordinates)

def drawLines():
    global vents
    for pair in listOfCoordinates:
        #prüfen ob X oder Y
        y1 = pair[0][0]
        x1 = pair[0][1]
        y2 = pair[1][0]
        x2 = pair[1][1]

        if y1 == y2:
            while x1 <= x2:
                vents[x1, y1] += 1
                x1 += 1

            y1 = pair[0][0]
            x1 = pair[0][1]
            y2 = pair[1][0]
            x2 = pair[1][1]
            while x2 <= x1:
                vents[x2, y1] += 1
                x2 += 1

            y1 = pair[0][0]
            x1 = pair[0][1]
            y2 = pair[1][0]
            x2 = pair[1][1]

        elif x1 == x2:
            while y1 <= y2:
                vents[x1, y1] += 1
                y1 += 1

            y1 = pair[0][0]
            x1 = pair[0][1]
            y2 = pair[1][0]
            x2 = pair[1][1]
            while y2 <= y1:
                vents[x1, y2] += 1
                y2 += 1

            #y1 = pair[0][0]
            #x1 = pair[0][1]
            #y2 = pair[1][0]
            #x2 = pair[1][1]

            x1 = pair[0][0]
            y1 = pair[0][1]
            x2 = pair[1][0]
            y2 = pair[1][1]


        elif x1 != x2 and y1 != y2:
            if x1 < x2 and y1 < y2:
                while x1 <= x2:
                    vents[x1, y1] += 1
                    x1 += 1
                    y1 += 1
                x1 = pair[0][0]
                y1 = pair[0][1]
                x2 = pair[1][0]
                y2 = pair[1][1]

            elif x1 < x2 and y1 > y2:
                while x1 <= x2:
                    vents[x1, y1] += 1
                    x1 += 1
                    y1 -= 1
                x1 = pair[0][0]
                y1 = pair[0][1]
                x2 = pair[1][0]
                y2 = pair[1][1]

            elif x1 > x2 and y1 < y2:
                while x1 >= x2:
                    vents[x1, y1] += 1
                    x1 -= 1
                    y1 += 1
                x1 = pair[0][0]
                y1 = pair[0][1]
                x2 = pair[1][0]
                y2 = pair[1][1]

            elif x1 > x2 and y1 > y2:
                while x1 >= x2:
                    vents[x1, y1] += 1
                    x1 -= 1
                    y1 -= 1
                x1 = pair[0][0]
                y1 = pair[0][1]
                x2 = pair[1][0]
                y2 = pair[1][1]


if __name__ == '__main__':
    readFile()
    drawLines()
    za = (vents > 1).sum()
    print("Number of critical Vents = " + str(za))
