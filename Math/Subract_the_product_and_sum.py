class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum =0
        while(n!=0):
            num = n%10
            product = product * num
            sum = sum + num
            n = n//10
        return product - sum    
        
        
solution = Solution()
result = solution.subtractProductAndSum(234)
print(result)
        