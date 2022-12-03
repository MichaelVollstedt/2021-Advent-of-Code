
def firstPart():
    horizontal = 0
    vertical = 0

    lines = open('02_advent','r')

    for line in lines:
        line = line.strip()
        commandString = line.split(' ', 1)
        print(commandString)

        if commandString[0] == 'forward':
            horizontal += int(commandString[1])
        elif commandString[0] == 'up':
            vertical -= int(commandString[1])
        else:
            vertical += int(commandString[1])

    print('horizontal = ' + str(horizontal))
    print('vertical = ' + str(vertical))
    print('multiplicate = ' + str(vertical * horizontal))

def secondPart():
    horizontal = 0
    depth = 0
    aim = 0

    lines = open('02_advent.txt', 'r')

    for line in lines:
        line = line.strip()
        commandString = line.split(' ', 1)
        print(commandString)

        if commandString[0] == 'forward':
            horizontal += int(commandString[1])
            depth += aim * int(commandString[1])
        elif commandString[0] == 'up':
            aim -= int(commandString[1])
        else:
            aim += int(commandString[1])

    print('horizontal = ' + str(horizontal))
    print('depth = ' + str(depth))
    print('multiplicate = ' + str(depth * horizontal))



if __name__ == '__main__':
    secondPart()
