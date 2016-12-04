# Part 1:

fileContent = open("day3-input.txt")
counter1 = 0
for i in fileContent:
    for a,b,c in [[int(j) for j in i.split()]]:
        if (a < b + c and b < c + a and c < a + b):
            counter1 += 1

print counter1

# Part 2:

fileContent = open("day3-input.txt").readlines()

tmpList = []
modList = []
modTmpList = []

for line in fileContent:
    tmpList.append([int(i) for i in line.strip().split()])

for i in xrange(0, len(tmpList) - 2, 3):
    for j in range(len(tmpList[i])):
        modTmpList.append(tmpList[i][j])
        modTmpList.append(tmpList[i + 1][j])
        modTmpList.append(tmpList[i + 2][j])
        modList.append(modTmpList)
        modTmpList = []

counter2 = 0

for k in modList:
    a = k[0]
    b = k[1]
    c = k[2]

    if (a < b + c and b < c + a and c < a + b):
        counter2 += 1
print counter2
