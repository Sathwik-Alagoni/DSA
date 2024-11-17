class Solution:
    def pivotInteger(self, n: int) -> int:
        x = ((n**2+n)/2)**0.5
        if x == int(x):
            return int(x)
        else:
            return -1
        
        


n = 4
solution = Solution()
result = solution.pivotInteger(n)
print(result) 