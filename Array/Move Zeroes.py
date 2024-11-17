from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i =0
        for j in range(len(nums)):
            if nums[i]==0 and nums[j]!=0:
                temp = nums[i]
                nums[i]=nums[j]
                nums[j]= temp
                i=i+1
            elif nums[i]!=0:
                i =i+1
                
        return nums      
        



solution = Solution()
nums =  [1,0,1]
result = solution.moveZeroes(nums)
print(result)
        