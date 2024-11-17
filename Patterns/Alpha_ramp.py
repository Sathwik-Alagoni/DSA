n = 4
ascii = 64
for i in range(n):
    for j in range(i):
        print(chr(ascii+i),end=" ")
    print()    