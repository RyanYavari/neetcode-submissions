class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, l = 0,0
        r = 1

        while r < len(prices):

            if prices[l] < prices[r]: # if theres a profit
                profit = prices[r]-prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            
            r += 1
        
        return maxProfit

        