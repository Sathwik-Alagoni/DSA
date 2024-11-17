r=5

for i in range(1,r+1):
    for j in range(1,r+1):
        if j==1 or i==r or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print() 