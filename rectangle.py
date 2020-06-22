import sys

if len(sys.argv)>1:
    c1 = sys.argv[1]
    c2 = sys.argv[2]
else:
    c1 = "resources/rectangle.txt"
    c2 = "resources/l6c7.txt"

file = open(c2)
fileRectangle = open(c1)

fileLines = file.read().splitlines()
rectangleLines = fileRectangle.read().splitlines()
j = 0

x = -1
y = -1
rectangleFound = False

for i in range(len(fileLines)):
    line = fileLines[i]
    lineToFind = rectangleLines[j]
    index = line.find(lineToFind)
    while (not rectangleFound) & (index != -1):
        searchIndex = index
        for k in range(len(rectangleLines)):
            k2 = k + i
            line = fileLines[k2]
            lineToFind = rectangleLines[k]
            index2 = line.find(lineToFind, searchIndex, searchIndex + len(lineToFind))
            if index2 != -1:
                rectangleFound = True
                x = index2 + 1
                y = i + 1
            else:
                rectangleFound = False
                break

        searchIndex += 1
        if searchIndex >= len(line):
            break
        else:
            index = line.find(lineToFind, searchIndex)
        if rectangleFound:
            break

if rectangleFound:
    print('Found!! at line ' + str(y) + " and column " + str(x))
else:
    print("Not Found!!!")

# print(file.readline()[3], end='')

file.close()
fileRectangle.close()
