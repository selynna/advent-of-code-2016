fileContent = open("day2-input.txt").read()
instrList = fileContent.rstrip().split('\n')

print instrList

keypad = []
keypad.append([1, 2, 3])
keypad.append([4, 5, 6])
keypad.append([7, 8, 9])

print keypad

code = []

startingRowPosition = 1
startingColPosition = 1

for i in range(len(instrList)):
    for j in range(len(instrList[i])):
        if instrList[i][j] == "L":
            if startingColPosition - 1 != -1:
                startingColPosition = startingColPosition - 1
        elif instrList[i][j] == "U":
            if startingRowPosition - 1 != -1:
                startingRowPosition = startingRowPosition - 1
        elif instrList[i][j] == "R":
            if startingColPosition + 1 != 3:
                startingColPosition = startingColPosition + 1
        else:
            if startingRowPosition + 1 != 3:
                startingRowPosition = startingRowPosition + 1

    code.append(keypad[startingRowPosition][startingColPosition])

print code

