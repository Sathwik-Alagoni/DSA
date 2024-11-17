class Solution:
    def minimumSum(self, num: int) -> int:      
        arr = []
        while(num!=0):
            rev = num%10
            arr.append(rev)
            num = num//10
        arr.sort()
        return (arr[0]*10+arr[3])+(arr[1]*10+arr[2])
    
num = 2436
solution = Solution()
result =  solution.minimumSum(num)
print(result)     