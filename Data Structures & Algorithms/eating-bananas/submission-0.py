class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''

        1   4   3   2

        output: minimum k such that all bananas are eaten < h hours

        for hour in range(h):
            choose a pile of bananas
            eat k banans from that pile
            if pile < k, finish eating pile but stay within poile

            1 <= k <= max(piles)

            find the minimum integer k to to eat all the bananas within h hnours

            find an integer in a sorted array given condition -> binary search

            constraint is h 

        
        implementation:

        binary search k to find the minimum k that eats all bananas in under h hours

        maxK = max(piles)
        left, right = 0, maxK
        k = maxK
        for k in range(1, maxK):
            mid = (left + right)//2

            if ate all bananas with k in <= h:
                right = mid - 1
                k = min(k, mid)
            else:
                left = mid + 1

        return k

        '''

        maxK = max(piles)
        left, right = 1, maxK
        k = maxK
        while left <= right:
            mid = (left + right)//2

            
            '''
            hours= 0
            while hours < = h
            loop through arr
            append to hours += divide by ceiling num/k 


            '''
            #calculate hours it takes to eat all banans in piles at banans-per-hour rate of k
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/mid)
            
            # if k is small enough to pass conditions, look for a smaller k
            if hours <= h:
                right = mid-1
                k = min(k, mid)
            else:
                left = mid + 1

        return k
    
    
        