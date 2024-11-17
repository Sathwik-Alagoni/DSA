#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while(num!=0):
            last = num%10
            sum = sum + last
            num = num//10
            if num ==0 and sum>=10:
                num = sum  
                sum = 0
        return sum    


solution = Solution()
result = solution.addDigits(0)
print(result)