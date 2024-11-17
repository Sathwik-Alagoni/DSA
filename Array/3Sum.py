from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
          
            b = i + 1
            c = len(nums) - 1
            
     
            while b < c:
                current_sum = nums[i] + nums[b] + nums[c]
                
                if current_sum == 0:
                    arr.append([nums[i], nums[b], nums[c]])
                    
                    
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                
            
                elif current_sum < 0:
                    b += 1
    
                else:
                    c -= 1
        
        return arr


nums = [0, 0, 0]
solution = Solution()
result = solution.threeSum(nums)
print(result)


        