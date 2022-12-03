from collections import Counter

#fileName = '08_advent_test.txt'
fileName = '08_advent.txt'
rawDigits = []
digits = []
codes = []

def readFile(rawDigits, digits, codes):
    lines = open(fileName, 'r')

    i = 0
    for line in lines:
        line = line.strip().split(' | ')
        rawDigits.append(line)

    for digit in rawDigits:
        x = digit[1].split(' ')
        digits.append(x)
        y = digit[0].split(' ')
        codes.append(y)


def countDigits(digits):
    count = 0

    for digit in digits:
        i = 0
        while i < 4:
            length = len(digit[i])
            # 7 = 3 digits
            # 4 = 4 digits
            # 1 = 2 digits
            # 8 = 7 digits
            if length == 2 or length == 3 or length == 4 or length == 7:
                count += 1
            i += 1

    return count

def sumOutputValues(digits, codes):
    number = 0

    indexDecoding = 0
    for digit in digits:
        toBeDecoded = codes[indexDecoding]
        decoding = decodeDigits(toBeDecoded)

        code = ''
        i = 0
        while i < 4:
            x = findDigit(digit[i], decoding)
            code += str(x)
            i += 1
        number += int(code)
        indexDecoding += 1

    return number

def findDigit(digitString, decoding):

    i = None
    for key in decoding:
        if len(decoding[key]) == len(digitString):
            if all(char in digitString for char in decoding[key]):
                i = int(key)
                break
    return i

def decodeDigits(codes):
    # codes e.g. ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
    decoded = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    i = None
    count = Counter()

    # reihenfolge ist wichtig!!!!
    for code in codes:
        length = len(code)

        if length == 2:
            i = 1
            decoded[i] = code
        elif length == 3:
            i = 7
            decoded[i] = code
        elif length == 4:
            i = 4
            decoded[i] = code
        elif length == 7:
            i = 8
            decoded[i] = code

    for code in codes:
        count.clear()
        count.update(code)
        length = len(code)

        # 2, 3, 5
        if length == 5:
            if all(char in code for char in decoded[7]):
                i = 3
                decoded[i] = code
            else:
                check = 0
                #counter = Counter(code)
                for char in decoded[4]:
                    if count[char] > 0:
                        check += 1
                if check == 3:
                    i = 5
                    decoded[i] = code
                elif check == 2:
                    i = 2
                    decoded[i] = code
        # 0, 6, 9
        elif length == 6:
            if all(char in code for char in decoded[4]):
                i = 9
                decoded[i] = code
            else:
                if all(char in code for char in decoded[1]):
                    i = 0
                    decoded[i] = code
                else:
                    i = 6
                    decoded[i] = code

    return decoded

if __name__ == '__main__':
    readFile(rawDigits, digits, codes)
    #count = countDigits(digits)
    #print(rawDigits)
    #print(digits)
    #print(codes)

    i = sumOutputValues(digits, codes)
    print(i)

