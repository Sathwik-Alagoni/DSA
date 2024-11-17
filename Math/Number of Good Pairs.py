from typing import List 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]==nums[j]:
                    count = count +1
        return count            

        




nums = [1,2,3,1,1,3]    
solution = Solution()
result = solution.numIdenticalPairs(nums)