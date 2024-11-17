def seeding(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if j<=i:
                print("*",end=" ")
        print()        
seeding(4)

def seeding(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if j<=i:
                print(j,end=" ")
        print()        
seeding(4)  
