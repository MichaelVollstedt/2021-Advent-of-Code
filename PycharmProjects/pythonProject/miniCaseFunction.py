
def stringRepeat(input):
    dict = {}

    for char in input:
        dict[char] = dict.get(char, 0) + 1
        #if char in dict:
        #    dict[char] += 1
        #else:
        #    dict[char] = 1

    print(dict)

if __name__ == '__main__':
    stringRepeat('hello world')
