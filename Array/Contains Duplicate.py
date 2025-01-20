from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for i in nums:
            if i in frequency:
                return True
            else:
                frequency[i]=1
        return False    

nums = [1,2,3,1]
solution= Solution()
result = solution.containsDuplicate(nums)
print(result)





#worst time complexity 

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False    
            


nums = [1,2,3,1]
solution= Solution()
result = solution.containsDuplicate(nums)
print(result)