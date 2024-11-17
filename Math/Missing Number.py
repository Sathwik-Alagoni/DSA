from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum =0
        for i in range(0,l):
           sum = sum + nums[i]
        return int((l*(l+1))/2 - sum)  
        




nums = [0,1]
solution = Solution()
result = solution.missingNumber(nums)
print(result)