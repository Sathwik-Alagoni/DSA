n =5
k=0
r=1
for i in range(n):
    for j in range(n):
        if j<=i:
            print(k,end="")
        k,r=r,k
    print()  