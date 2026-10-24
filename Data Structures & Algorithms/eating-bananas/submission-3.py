class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        maxK = max(piles)

        lo, hi = 0, maxK
        k = 0

        while lo <= hi:
            k = (lo+hi)//2
        
            countHours = 0

            loop through piles:
                calc sum of countHours

            if countHours > h: # if the nubmer of hours to eat all bananas exceeds h, then we must increase k
                lo = k + 1
            elif countHours <= h: #if the num of hours to eat all bananas is less or equal to h, then we must search for a smaller k
                hi = k - 1
        


        return k

        '''

        maxK = max(piles) #returns highest num in piles
        lo, hi = 1, maxK
        k = maxK

        while lo <= hi:
            mid = (lo+hi)//2

            countHours = 0

            for bananas in piles:
                countHours += math.ceil(bananas/mid) #counts how many hours it takes to eat all the bananas in a pile 
            
            if countHours > h:
                lo = mid+1
            else:
                hi = mid-1
                k = min(mid, k) 
        
        return k



            
        