import sys

n = int(sys.argv[1])

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    if i != n - 1:
        print()
