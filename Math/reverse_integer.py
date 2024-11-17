class Solution:
    def reverse(self, x: int) -> int:
        sum =0
        num = x
        if x<0:
            x = -1*x
        while(x!=0):
            val = x%10
            sum = sum*10+val
            x=x//10
        if sum>2**31-1 or sum<-2**31:
            return 0
        elif num<0:
            return sum*-1
        else:
            return sum    

x=123
solution =Solution()
result = solution.reverse(x)