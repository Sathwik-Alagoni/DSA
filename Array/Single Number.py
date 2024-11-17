#using dictonary 
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict= {}
        for frequency in nums:
            if frequency in dict:
                dict[frequency]+=1
            else:
                dict[frequency]=1
        
        for key,value in dict.items():
            if value==1:
                return key

nums = [4,1,2,1,2]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
        

#using array frequency 
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        offset = 30000  
        maxvalue = 60000 
        frequency = [0] * (maxvalue + 1)  

        
        for num in nums:
            frequency[num + offset] += 1

       
        for i in range(len(frequency)):
            if frequency[i] == 1:
                return i - offset  

nums = [-1, -1, -2]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
"""        


#using sort and pointer
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i =0
        while(i<len(nums)-1):
            if nums[i]==nums[i+1]:
                i= i +2
            else:
                return nums[i]
        return nums[i]
nums = [4,1,2,1,2]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
"""