fileContent = open("day3-input.txt")

counter = 0
for i in fileContent:
    for a,b,c in [[int(j) for j in i.split()]]:
        if (a < b + c and b < c + a and c < a + b):
            counter += 1

print counter
