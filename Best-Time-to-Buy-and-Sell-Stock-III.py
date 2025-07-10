class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 =  0  #first trans 
        dp1 = -prices[0] # first buy
        dp2 =  0  # First Sell
        dp3 = -prices[0] # second buy 
        dp4 = 0 #seconed sell
        for price in prices: 
            dp1 = max(dp1, dp0 - price) 
            dp2 = max(dp2 , dp1 + price) 
            dp3 = max(dp3, dp2 - price) 
            dp4 = max(dp4 , dp3 + price)
        return dp4
        




        