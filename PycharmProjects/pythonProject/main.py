# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def firstPart():
    prev = None
    p1 = 0

    #file1 = open('01_advent.txt','r')
    #lines = file1.readLines()
    lines = open('01_advent.txt','r')
    #file1.close()

    for line in lines:
        line = line.strip()
        x = int(line)
        if prev and x > prev:
            p1 += 1
        prev = x
    print(p1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #firstPart()
    p1 = 0
    p2 = 0
    XS = [int(x) for x in open('01_advent.txt','r')]
    for i in range(len(XS)):
        if i >= 1 and XS[i]
    print(XS)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


