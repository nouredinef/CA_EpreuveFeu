import sys

text=sys.argv[1]
#text="Bonzdljkh!:?.QS/sdmih azdqd kl"

i=0
for char in text:
    if i%2!=0:
        print(char.capitalize(), end="")
    else:
        print(char.casefold(), end="")
    if char!=" ":
        i=i+1