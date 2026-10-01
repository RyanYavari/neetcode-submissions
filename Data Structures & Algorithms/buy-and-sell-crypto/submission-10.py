class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        '''
        prices = [10,1,5,6,7,1]
                    l      r
        profit = 4, 5, 6

        l, r = 0, 0

        while r < len(prices)
        if prices[r] < prices[l]:
            l = r
        
        profit = max(profit,prices[r]-prices[l])



        return profit

        '''

        l, r = 0, 0
        profit = 0

        while r < len(prices):
            
            if prices[r] < prices[l]:
                l = r
            
            #if prices[r] > prices[l] and l < r, profit exists, calculate
            if l < r:
                profit = max(profit, prices[r]-prices[l])
            r += 1
        
        return profit

        '''
        [10 1   5   6   7   1]
        l
        r

        profit = 4, 5, 6




        '''
            
                


            
            
            



        







        