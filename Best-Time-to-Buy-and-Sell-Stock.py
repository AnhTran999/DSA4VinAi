class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)] #create dp 2d matrix
        dp[0][0] = 0 # do nothing in day 1 
        dp[0][1] = -prices[0] # if buy stock on day 1
        for i in range(1,n): 
            dp[i][0] = max(dp[i-1][0] , dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i] )
        return dp[n-1][0] 
        