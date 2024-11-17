n = 4
ascii = 65
k=0
count =0
for i in range(n,0,-1):
    for j in range(1,n+n+1):
        if  j>=i and j<=(i+2*k):
            print(chr(ascii+count),end=" ")
            count = count +1    
        else:
            print(" ",end=" ")
      
    print()    
    k=k+1  