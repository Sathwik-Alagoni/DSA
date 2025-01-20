class Solution:
    def findMinDiff(self, arr,M):
        n = M-1
        diff = 0
        arr.sort()
        mindif = float('inf')
        for i in range(len(arr)-M+1):
            diff = arr[n]-arr[i]
            if diff<mindif:
                mindif=diff
            n=n+1
        return mindif    
        
solution = Solution()
arr = [11,13,7,5,13,12]
m = 4
result = solution.findMinDiff(arr,m)
print(result)