class Solution:
    def countDigits(self, num: int) -> int:
        divnum = num
        count =0
        while(num!=0):
            n = num % 10
            if(divnum % n ==0):
                count = count +1
            num = num//10    
        return count    
            
        
solution = Solution()
result = solution.countDigits(7)
print(result)