class Solution:
    def isThree(self, n: int) -> bool: 
        num = n
        count =0
        for i in range(1,int(n**0.5)+1):
            if num%i ==0: 
                if i== num //i:
                    count = count +1
                else:
                    count = count +2
        if count==3:
            return True
        else:
            return False
            
        
solution = Solution()
result = solution.isThree(4)
print(result)