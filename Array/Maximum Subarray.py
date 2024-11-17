from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            current_max = nums[0]
            global_max = nums[0]

            for i in range(1,len(nums)):
                current_max = max(nums[i],current_max+nums[i])
                if current_max > global_max:
                    global_max = current_max
            return global_max        

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
result = solution.maxSubArray(nums)
print(result)