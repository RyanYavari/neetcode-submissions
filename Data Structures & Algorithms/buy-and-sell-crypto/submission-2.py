class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window 
            # left is day to buy
            # right is day to sell if profit > maxProfit. defaults 0
        # initialize maxProfit = 0
        # difference = right - left
        # left = 0

        maxProfit, left, profit = 0, 0, 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
            

        
        