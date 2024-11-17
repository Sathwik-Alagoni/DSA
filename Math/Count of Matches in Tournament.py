class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum = 0
        while n!=1:
            if n % 2 ==0:
                sum += n/2
                n = n/2
            else:
                sum += (n-1)/2
                n = (n+1)/2
        return int(sum)        
            


n= 7
solution = Solution()
result = solution.numberOfMatches(n)
print(result)