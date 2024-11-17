from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        count = 0
        sum =0 
        actual_sum = 0
        for i in nums:
            for j in range(1,round(i**0.5)+1):
                if i%j==0:
                    val = i//j
                    if j==val:
                        count= count +1
                    else:    
                        count = count +2
                    sum = sum+j+val
            if count ==4:
                actual_sum = actual_sum+sum
            sum = 0
            count =0
        return actual_sum

nums = [21,4,7]
solution = Solution()
result = solution.sumFourDivisors(nums)
print(result) 