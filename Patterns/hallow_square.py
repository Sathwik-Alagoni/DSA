
r=10
for i in range(r+1):
    for j in range(r+1):
        if i==0 or i==r or j==0 or j==r:
            print("* ",end="")
        else:
            print("  ",end="")
    print()   