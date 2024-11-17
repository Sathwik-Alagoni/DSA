class Solution:
    def twoSum(self,nums,target):
        frequency = []
        for i in range(len(nums)):
            frequency.append([nums[i],i])
    
        frequency.sort()
      

 
        l = 0
        r = len(nums)-1
        while(l<r):
            su = frequency[l][0]+frequency[r][0]
            if su == target:
                lis = [frequency[l][1],frequency[r][1]]
                return lis
            elif su>target:
                r=r-1
            else:
                l=l+1

nums = [3,3]
target= 6
l=len(nums)
solution = Solution()
result = solution.twoSum(nums, target)

print(result) 