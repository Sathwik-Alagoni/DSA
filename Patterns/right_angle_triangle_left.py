def nForest(n:int) ->None:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=i:
                print("* ",end="")
        print()
        
nForest(4)        
        
        
def nForest(n:int) ->None:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=i:
                print(j,end=" ")
        print()
        
nForest(4)  


def nForest(n:int) ->None:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=i:
                print(i,end=" ")
        print()
        
nForest(4) 

