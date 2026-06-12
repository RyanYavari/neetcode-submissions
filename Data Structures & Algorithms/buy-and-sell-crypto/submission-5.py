class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''

        maxVal = float(-inf)
        profit = 0
        l = 0

        for r, price in enumerate(prices):
            
            if right pointer price is less than left, left = right
            
            if right pointer price is more than maxPrice and right pointer > left pointer, maxPrice = right pointer price
                calculate the profit 
            
        return profit
        '''

        maxPrice = float("-inf")
        profit = 0
        l = 0

        for r, price in enumerate(prices):
            if price < prices[l]:
                l = r
            if r > l:
                
                profit = max(profit, price-prices[l])
        
        return profit


        