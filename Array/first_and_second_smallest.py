class Solution:
    def minAnd2ndMin(self, arr):
        small_num = float('inf')
        second_small = float('inf')
        
        for i in range(len(arr)):
            if small_num>arr[i]:
                second_small=small_num
                small_num=arr[i]
            elif small_num<arr[i]<second_small:
                second_small=arr[i]
    
        if second_small==float('inf'):
            return [-1,-1]
        
                
        return [small_num,second_small]        


arr = [2,4,3,5,6]
solution = Solution()
result = solution.minAnd2ndMin(arr)