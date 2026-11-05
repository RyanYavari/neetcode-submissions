class Solution:
    def search(self, nums: List[int], target: int) -> int:


        '''
        



        '''

        n = len(nums)
        lo, hi = 0, n-1

        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] <= nums[hi]: #right side is sorted 
                if nums[mid] < target <= nums[hi]: #target is in right side, search right 
                    lo = mid+1
                else: #target is in left side, search left
                    hi = mid-1
            
            elif nums[mid] > nums[hi]: # left side is sorted
                if nums[lo] <= target < nums[mid]: #target is in left side, search left
                    hi = mid-1
                else: #target is in right side, search right
                    lo = mid+1
            
        
        return -1
        