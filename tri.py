import sys

numbers=[int(i) for i in sys.argv[1:]]

#numbers = [1, 2, 3, 5, 4, 9, 20, 1, 5]
change= True

k = 0

print(numbers)
while change:
    change=False
    for i in range(len(numbers)-1):
        if numbers[i+1]>numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            change = True
    k = k+1

print(numbers)
