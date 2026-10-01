class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''

        finding range -> two pointers
        maxArea = (r-l)*min(heights[l],heights[r])


        l, r = 0, len(heights)-1

        while l < r:

            calculate area

            if height of l < height of r: 
                l++
            if height of r < height of left or equal:
                r--
            
            maxArea = max(maxArea, area)


        return maxArea


        '''


        l, r = 0, len(heights)-1
        maxArea = float('-inf')
        
        while l < r:
            area = (r-l)*min(heights[r], heights[l])

            if heights[l] < heights[r]: #if left is smaller, explore on left
                l += 1
            else:
                r -= 1
        
            maxArea = max(maxArea, area)
        
        return maxArea


        '''

        [1,7,2,5,4,7,3,6]
           l         r
        maxArea = 3


        '''






        