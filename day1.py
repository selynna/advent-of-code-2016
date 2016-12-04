# import file

fileInput = open("day1-input.txt").read()
directionList = fileInput.split(", ")

eastBlocks = 0
westBlocks = 0
northBlocks = 0
southBlocks = 0
directionIndex = 0

grid = []

startingRowPosition = 0
startingColumnPosition = 0

for i in directionList:
    if i[:1] == "R":
        directionIndex += 1
        if directionIndex == 4:
            directionIndex = 0
    else:
        directionIndex -= 1
        if directionIndex == -1:
            directionIndex = 3
    j = 0
    k = 0
    l = 0
    m = 0

    if directionIndex == 0:
        northBlocks += (int)(i[1:])
        for j in range((int)(i[1:])):
            startingRowPosition -= 1
            pos = str(startingRowPosition) + " " + str(startingColumnPosition)
            if pos in grid:
                print abs(startingRowPosition) + abs(startingColumnPosition)
            grid.append(pos)

    elif directionIndex == 1:
        eastBlocks += (int)(i[1:])
        for k in range((int)(i[1:])):
            startingColumnPosition += 1
            pos = str(startingRowPosition) + " " + str(startingColumnPosition)
            if pos in grid:
                print abs(startingRowPosition) + abs(startingColumnPosition)
            grid.append(pos)
    elif directionIndex == 2:
        southBlocks += (int)(i[1:])
        for l in range((int)(i[1:])):
            startingRowPosition += 1
            pos = str(startingRowPosition) + " " + str(startingColumnPosition)
            if pos in grid:
                print abs(startingRowPosition) + abs(startingColumnPosition)
            grid.append(pos)
    else:
        westBlocks += (int)(i[1:])
        for m in range((int)(i[1:])):
            startingColumnPosition -= 1
            pos = str(startingRowPosition) + " " + str(startingColumnPosition)
            if pos in grid:
                print abs(startingRowPosition) + abs(startingColumnPosition)
            grid.append(pos)


horizontalBlocks = eastBlocks - westBlocks
verticalBlocks = northBlocks - southBlocks

totalBlocks = abs(horizontalBlocks) + abs(verticalBlocks)
print totalBlocks
