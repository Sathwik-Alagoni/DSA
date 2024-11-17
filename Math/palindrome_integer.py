class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum =0
        num = x
        if x<0:
            x = -1*x
        while(x!=0):
            val = x%10
            sum = sum*10+val
            x=x//10
        if sum>2**31-1 or sum<-2**31:
            return False
        
        
        if sum == num  and num>0 or num==0:
            return True
        else:
            return False

x=222
solution =Solution()
result = solution.isPalindrome(x)
print(result)