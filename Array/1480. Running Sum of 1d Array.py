from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n =len(nums)
        sum =0
        num = []
        for i in range(n):
            sum = sum +nums[i]
            num.append(sum)
        
        return num    



nums = [1,2,3,4]
solution = Solution()
result = solution.runningSum(nums)
print(result)
        