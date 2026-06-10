class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # the goal is to find the pair with the largest minimum

        # traverse array with left and right pointers
        
        # find the largest number, then find the second largest
        

        # return the product of two indices values

        l = 0
        r = len(heights)-1
        maxVol = 0

        while l < r:
            distance = r-l
            vol = min(heights[l], heights[r])*distance
            if vol > maxVol:
                maxVol = vol

            if heights[r] > heights[l]:
                l+= 1
            elif heights[r] < heights[l]:
                r-= 1
            else:
                l+=1 
        
        return maxVol
            

            

            
        