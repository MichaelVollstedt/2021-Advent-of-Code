from collections import Counter

inputList = []
fileName = '03_advent.txt'

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def readBinaryList():
    global inputList
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        binaryList = list(line)

        if not inputList:
            for a in range(len(binaryList)):
                inputList.append([])
                #print(inputList)

        i = 0
        for x in binaryList:
            inputList[i].append(x)
            i += 1
   #print(inputList)

def oxigenRating():
    resultOxigen = ''
    binaryCodeList = []
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        binaryCodeList.append(str(line))

    #print('----- binary Code List -----')
    #print(binaryCodeList)

    readBinaryList()
    #print('----- binary List -----')
    #print(inputList)

    whichBinary = ''
    for list in inputList:
        if list.count('1') > list.count('0'):
            whichBinary = '1'
        elif list.count('1') == list.count('0'):
            whichBinary = 'equal'
        else:
            whichBinary = '0'

        #print('whichBinary = ' + whichBinary)

        i = 0
        if whichBinary != 'equal':
            for binary in list:
                if binary != whichBinary:
                    for list in inputList:
                        list[i] = ''
                i += 1
        else:
            for binary in list:
                if binary == '0':
                    for list in inputList:
                        list[i] = ''
                i += 1

        #print('Inputlist = ' + str(inputList))
        #print(binaryCodeList)

    i = 0
    for list in inputList:
        inputList[i] = remove_values_from_list(list, '')
        i += 1

    #print('Inputlist = ' + str(inputList))

    for list in inputList:
        for x in list:
            resultOxigen += str(x)

    return resultOxigen

def dioxidRating():
    resultDioxid = ''
    binaryCodeList = []
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        binaryCodeList.append(str(line))

    print('----- binary Code List -----')
    print(binaryCodeList)

    readBinaryList()
    print('----- binary List -----')
    print(inputList)

    whichBinary = ''
    for list in inputList:
        #abort if it is the last binary in the list
        if list.count('1') == 0 and list.count('0') == 1:
            break
        elif list.count('1') == 1 and list.count('0') == 0:
            break

        if list.count('1') > list.count('0'):
            whichBinary = '0'
        elif list.count('1') == list.count('0'):
            whichBinary = 'equal'
        else:
            whichBinary = '1'

        print('whichBinary = ' + whichBinary)

        i = 0
        if whichBinary != 'equal':
            for binary in list:
                if binary != whichBinary:
                    for list in inputList:
                        list[i] = ''
                i += 1
        else:
            for binary in list:
                if binary == '1':
                    for list in inputList:
                        list[i] = ''
                i += 1

        print('Inputlist = ' + str(inputList))
        print(binaryCodeList)

    i = 0
    for list in inputList:
        inputList[i] = remove_values_from_list(list, '')
        i += 1

    print('Inputlist = ' + str(inputList))

    for list in inputList:
        for x in list:
            resultDioxid += str(x)

    print(resultDioxid)
    return resultDioxid



def firstPart():
    resultGamma = ''
    resultEpsilon = ''

    readBinaryList()

    for list in inputList:

        if list.count('1') > list.count('0'):
            resultGamma += '1'
        else:
            resultGamma += '0'

    print(resultGamma)
    print(int(resultGamma, 2))

    for x in str(resultGamma):
        if x == "0":
            resultEpsilon += "1"
        else:
            resultEpsilon += "0"
    print(resultEpsilon)
    print(int(resultEpsilon, 2))

    energy = int(resultGamma, 2) * int(resultEpsilon, 2)
    print('Energy: ' + str(energy))


def secondPart():
    resultOxigen = int(oxigenRating(),2)
    resultDioxide = int(dioxidRating(), 2)

    print(resultOxigen)
    print(resultDioxide)


    lifeSupportRating = resultOxigen * resultDioxide
    print('Life Support Rating: ' + str(lifeSupportRating))


if __name__ == '__main__':
    #firstPart()
    secondPart()
