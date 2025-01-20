class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_window = 0
        frequency = {}
        for j in range(len(s)):
            if s[j] in frequency:
                frequency[s[j]]+=1
            else:
                frequency[s[j]]=1
        
            max_frequency = max(frequency.values())
            window_size = j - i + 1
        
            if window_size-max_frequency>k:
                frequency[s[i]]-=1
                i+=1
            max_window = max(max_window, j - i + 1)    
         
                
        return max_window    
        
        
        
        


s = "ABAB"
k = 2        
solution = Solution()
result = solution.characterReplacement(s,k)
print(result)
        