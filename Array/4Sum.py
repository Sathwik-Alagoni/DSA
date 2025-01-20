from typing import List 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l= j+1
                r = n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        arr.append([nums[i],nums[j],nums[l],nums[r]])
                        r=r-1
                        l = l+1
                        while l<r and nums[l]==nums[l-1]:
                            l = l+1
                        while l<r and nums[r]==nums[r+1]:
                            r=r-1
                    elif total>target:
                        r=r-1
                        
                    else:
                        l=l+1
                            
                        
        return arr
        
        
nums = [1,0,-1,0,-2,2]
target = 0        
solution = Solution()
result = solution.fourSum(nums,target)
print(result)

