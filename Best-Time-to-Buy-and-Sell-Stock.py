class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        cash = 0 
        for price in prices[1:]: 
            hold = max(hold, -price)
            cash = max(cash, price + hold)
        return cash
        