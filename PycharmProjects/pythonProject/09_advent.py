import numpy

heights = []
fileName = '09_advent.txt'

def readFile():
    global heights
    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip()
        heights.append(line)

    for i, x in enumerate(heights):
        heights[i] = [int(char) for char in x]



def getAdjacentElements(heights):
    lows = []

    for i_line, line in enumerate(heights):

        for i_element, element in enumerate(line):
            prevLine = None
            nextLine = None
            prevNumberInLine = None
            nextNumberInLine = None
            values = []

            try:
                prevLine = heights[i_line - 1][i_element]
                values.append(prevLine)
            except:
                prevLine = None
            try:
                nextLine = heights[i_line + 1][i_element]
                values.append(nextLine)
            except:
                nextLine = None
            try:
                prevNumberInLine = heights[i_line][i_element - 1]
                values.append(prevNumberInLine)
            except:
                prevNumberInLine = None
            try:
                nextNumberInLine = heights[i_line][i_element + 1]
                values.append(nextNumberInLine)
            except:
                nextNumberInLine = None


            miniumum = min(values)
            if element < miniumum:
                lows.append(element)

    return lows

def floodFillRecursion(i_element, i_line, heights, count):

    if heights[i_line][i_element] != 9:
        count += 1
        heights[i_line][i_element] = 9

        try:
            # vorherige Reihe
            if i_line > 0:
                prevLine = i_line - 1
                prevLineValue = heights[prevLine][i_element]
                if prevLineValue != 9:
                    count = floodFillRecursion(i_element, prevLine, heights, count)
        except:
            prevLine = None
        try:
            # nächste Reihe
            if i_line < len(heights) - 1:
                nextLine = i_line + 1
                nextLineValue = heights[nextLine][i_element]
                if nextLineValue != 9:
                    count = floodFillRecursion(i_element, nextLine, heights, count)
        except:
            nextLine = None
        try:
            # vorheriges Element
            if i_element > 0:
                prevElementPos = i_element - 1
                prevNumberValue = heights[i_line][prevElementPos]
                if prevNumberValue != 9:
                    count = floodFillRecursion(prevElementPos, i_line, heights, count)
        except:
            prevNumberInLine = None
        try:
            # nächstes Element
            if i_element < len(heights[i_line]) - 1:
                nextElementPos = i_element + 1
                nextNumberValue = heights[i_line][nextElementPos]
                if nextNumberValue != 9:
                    count = floodFillRecursion(nextElementPos, i_line, heights, count)
        except:
            nextNumberInLine = None

    return count


if __name__ == '__main__':
    readFile()
    print(heights)
    #part 1
    #lows = getAdjacentElements(heights)
    #print(lows)
    #risk = [x + 1 for x in lows]
    #riskValue = sum(risk)
    #print(riskValue)

    #part 2
    basins = []
    for i_line, line in enumerate(heights):
        for i_element, element in enumerate(line):
            count = 0
            count = floodFillRecursion(i_element, i_line, heights, count)
            if count > 0:
                basins.append(count)

    basins.sort()
    length = len(basins)
    result1 = basins[length-1] * basins[length-2] * basins[length-3]
    print('Result = ' + str(result1))