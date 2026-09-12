class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        '''
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):

            if price of left is less than price of right:
                l = r
            else:
                calculate profit
            r++
        
        return profit

        '''

        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            # if sell day is less than buy day, buy day -> sell day
            # if prices[r] < prices[l], r = l
            if prices[l] > prices[r]:
                l = r

            #sell day is higher than buy day (r > l)   
            else:
                profit = prices[r]-prices[l]
                maxProfit = max(maxProfit, profit)
            r += 1
        return maxProfit

                