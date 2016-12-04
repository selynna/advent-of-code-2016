fileContent = open("day2-input.txt").read()
instrList = fileContent.rstrip().split('\n')

keypad = []
# keypad.append([1, 2, 3])
# keypad.append([4, 5, 6])
# keypad.append([7, 8, 9])
keypad.append([0, 0, 1, 0, 0])
keypad.append([0, 2, 3, 4, 0])
keypad.append([5, 6, 7, 8, 9])
keypad.append([0, "A", "B", "C", 0])
keypad.append([0, 0, "D", 0 , 0])


code = []

startingRowPosition = 2
startingColPosition = 0

for i in range(len(instrList)):
    for j in range(len(instrList[i])):
        if instrList[i][j] == "L":
            if startingColPosition - 1 >= 0 and startingColPosition - 1 < 5 and keypad[startingRowPosition][startingColPosition - 1] != 0:
                startingColPosition = startingColPosition - 1
        elif instrList[i][j] == "U":
            if startingRowPosition - 1 >= 0 and startingRowPosition - 1 < 5 and keypad[startingRowPosition - 1][startingColPosition] != 0:
                startingRowPosition = startingRowPosition - 1
        elif instrList[i][j] == "R":
            if startingColPosition + 1 >= 0 and startingColPosition + 1 < 5 and keypad[startingRowPosition][startingColPosition + 1] != 0:
                startingColPosition = startingColPosition + 1
        else:
            if startingRowPosition + 1 >= 0 and startingRowPosition + 1 < 5 and keypad[startingRowPosition + 1][startingColPosition] != 0:
                startingRowPosition = startingRowPosition + 1

    code.append(keypad[startingRowPosition][startingColPosition])

print code

