class Solution:
    def longestKSubstr(self, s, k):
        i = 0
        max_window = -1
        frequency = {}
        m =0
        for j in range(len(s)):
            if s[j] in frequency:
                frequency[s[j]]+=1
            else:
                frequency[s[j]]=1
                m+=1
        
            if m>k:
                frequency[s[i]]-=1
                if frequency[s[i]]==0:
                    m=m-1
                i=i+1    
            
            if m==k:    
                max_window = max(max_window,j-i+1) 
                
        return max_window    
        
        
        
        

s = "aabacbebebe"
k = 3      
solution = Solution()
result = solution.longestKSubstr(s,k)
print(result)

