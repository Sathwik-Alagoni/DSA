n = 4
ascii = 65
for i in range(n):
    for j in range(i):
        print(chr(ascii+j),end=" ")
    print()  


n = 4
ascii = 65
for i in range(n,-1,-1):
    for j in range(i):
        print(chr(ascii+j),end=" ")
    print()       