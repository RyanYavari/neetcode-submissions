class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''

        we know that sorted segments have the lowest value on the left

        minVal = float('inf')

        n = len(nums)
        lo, hi = 0, n-1

        while lo <= hi:
            mid -= (lo+hi)//2

           

        
        return minVal


        '''

        minVal = nums[0]

        n = len(nums)
        lo, hi = 0, n-1

        while lo < hi:
            mid = (lo+hi)//2
            minVal = min(minVal, nums[mid])

            if nums[mid] > nums[hi]: #lowest value on right
                lo = mid+1
            elif nums[mid] < nums[hi]: #lowest value on left
                hi = mid
            minVal = min(minVal, nums[lo])

        return minVal



