from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n<k:
            return 0
        l =0 
        r=k-1
        sum = 0
        count = 0
        for i in range(k):
            sum = sum+ arr[i]
        if sum>=threshold*k:
            count = count +1
        sum = sum - arr[l]
        l= l+1
        r=r+1
        for i in range(1,n-k+1):
            sum = sum+arr[r]
            if sum>=threshold*k:
                count = count +1
            sum = sum-arr[l]
            l = l+1
            r = r+1
        return count    

arr =[11,13,17,23,29,31,7,5,2,3]
k = 3 
threshold = 5      
solution = Solution()
result =solution.numOfSubarrays(arr,k,threshold)
print(result)