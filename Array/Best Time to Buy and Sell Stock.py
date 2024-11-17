from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float("inf")
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
            elif prices[i]-minPrice>maxProfit:
                maxProfit = prices[i]-minPrice
        return(maxProfit)        

prices = [2,1,2,1,0,1,2]
solution = Solution()
result = solution.maxProfit(prices)
print(result)