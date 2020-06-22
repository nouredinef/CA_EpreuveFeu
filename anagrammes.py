import sys

if len(sys.argv)>1:
    inputWord = sys.argv[1]
    file = sys.argv[2]
else:
    inputWord = "arrbe"
    file = "./resources/anagrammesListeFr.txt"

wordList = open(file).read().splitlines()

result = []

for word in wordList:
    if len(word) != len(inputWord):
        continue
    elif sorted(word) == sorted(inputWord):
        result.append(word)

print(result)
