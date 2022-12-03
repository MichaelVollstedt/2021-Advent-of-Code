import numpy as np

fileName = '04_advent_test.txt'
bingoNumbers = []
rawBingoBoards = []
bingoBoardsList = {}

bingoBoardsArray = {}
bingoDrawnNumbersArray = {}

def readFileAndCreateRawBingo():
    global bingoNumbers
    global rawBingoBoards

    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip()

        if i == 0:
            bingoNumbers = line.split(',')
        else:
            line = line.split()
            map_object = map(int, line)
            list_of_integers = list(map_object)
            rawBingoBoards.append(list_of_integers)

        i += 1
    #rawBingoBoards = [elem for elem in rawBingoBoards if elem != '']
    rawBingoBoards = [elem for elem in rawBingoBoards if elem != []]
    #print(rawBingoBoards)

def createBingoBoards():
    global bingoBoardsList
    global bingoBoardsArray
    global bingoDrawnNumbersArray

    lengthBoards = len(rawBingoBoards)
    #print("länge = " + str(lengthBoards))
    countBoards = int(lengthBoards / 5)
    #print("Anzahl der Boards = " + str(countBoards))

    keyName = 1
    i = 0
    a = 0
    e = 5
    while i < countBoards:
        bingoBoardsList[keyName] = rawBingoBoards[a:e]
        #print('Hier ist das Raw Board = ' + str(i) + '\n' + str(rawBingoBoards[a:e]))
        bingoBoardsArray[keyName] = np.asarray(bingoBoardsList[keyName])
        bingoDrawnNumbersArray[keyName] = np.zeros((5,5) , dtype=int)
        i += 1
        a += 5
        e += 5
        keyName += 1

    #print('>>>>> bingoBoardsArray = \n' + str(bingoBoardsArray))

def checkBoardForNumber(bingoBoard, number):
    ret = []

    result = np.where(bingoBoard == number)
    print('Check ' + str(number))
    print(result)
    if number == 25:
        text = 1
    temp = result[0]

    if result:
        row = int(result[0])
        column = int(result[1])
        ret = [row, column]
        print(' Found one !!! for Number ' + str(number) + ' = ' + str(ret))

    return ret

def drawBingoNumbers():
    global bingoDrawnNumbersArray
    print('Hier sind die Raw Bingo Boards = ' + '\n' + str(rawBingoBoards))
    print('Hier sind die Bingo Boards = ' + '\n' + str(bingoBoardsArray))

    for number in bingoNumbers:
        print('----- Lets check number ' + str(number) + ' -----')
        keyName = 1

        length = len(bingoBoardsArray)
        while keyName <= length:
            bingoBoard = bingoBoardsArray[keyName]
            print('Das folgende Board wird geprüft' + '\n' + str(bingoBoard))
            result = checkBoardForNumber(bingoBoard, int(number))
            print('Result = ' + str(result))

            if result:
                row = result[0]
                column = result[0]
                bingoDrawnNumbersArray[keyName][row, column] = 1

            keyName += 1


        #for bingoBoard in bingoBoardsArray:
        #   print('Das folgende Board wird geprüft' + '\n' + str(bingoBoard))
        #    result = checkBoardForNumber(bingoBoard, number)
        #    print('Result = ' + str(result))

        #   if result[0]:
                #need to find a way to update list in key
        #        bingoDrawnNumbersArray[keyName][result[0], result[1]] = 1

        #    keyName += 1



if __name__ == '__main__':
    readFileAndCreateRawBingo()
    createBingoBoards()

    #checkBoardForNumber(bingoBoardsArray[1], 23)
    #print('-------- Bingo Boards Array --------' + '\n' + str(bingoBoardsArray))
    #print('First Bingo Board = ' + '\n' + str(bingoBoardsArray[1]))
    #print('Drawn Numbers Bingo Board = ' + '\n' + str(bingoDrawnNumbersArray))

    drawBingoNumbers()
    print(bingoDrawnNumbersArray)

