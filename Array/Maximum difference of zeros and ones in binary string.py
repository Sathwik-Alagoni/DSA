class Solution:
    def maxSubstring(self, S):
        m = 1 if S[0] == '0' else -1
        
        current_count = m
        global_count = m
        
        
        for i in range(1, len(S)):
            num = 1 if S[i] == '0' else -1  
            current_count = max(num, num + current_count)
            global_count = max(global_count, current_count)
        
        return global_count