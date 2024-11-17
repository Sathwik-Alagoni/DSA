
ascii = 64
n=3
count =0
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j>=i:
            print(chr(ascii+i),end=" ")
    print()    
        