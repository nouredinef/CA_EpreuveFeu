import sys

# n=sys.argv[1]

n=42
def factoriel(num):
    if num == 0:
        return 1
    return num*factoriel(num - 1)


print(factoriel(n))

