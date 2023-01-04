n = int(input("Height: "))
i = 0
j = 0
for i in range(8):
    i = i + 1
    for k in range(i):
        k=k-1
        print(" ")
    for j in range(i):
        j=j+1
        print("#", end="")
        print()