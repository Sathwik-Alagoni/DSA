from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      
        if len(p) > len(s):
            return []
        
        frequency = {}
        for i in range(len(p)):
            if p[i] in frequency:
                frequency[p[i]] += 1
            else:
                frequency[p[i]] = 1
        
        cfrequency = {}
        l = 0
        r = len(p)
        
 
        for i in range(l, r):
            if s[i] in cfrequency:
                cfrequency[s[i]] += 1
            else:
                cfrequency[s[i]] = 1
        
   
        arr = []
        
        if frequency == cfrequency:
            arr.append(0)

        while r < len(s):
          
            if s[r] in cfrequency:
                cfrequency[s[r]] += 1
            else:
                cfrequency[s[r]] = 1
            
            cfrequency[s[l]] -= 1
            if cfrequency[s[l]] == 0:
                cfrequency.pop(s[l], None)
        
            if frequency == cfrequency:
                arr.append(l + 1) 

            l += 1
            r += 1
        
        return arr


s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"
solution = Solution()
result = solution.findAnagrams(s, p)
print(result)  
