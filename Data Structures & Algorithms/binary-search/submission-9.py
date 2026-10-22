class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target: #if mid == target, return index
                return mid
            
            elif target > nums[mid]: #target greater than mid, ignore lower half
                lo = mid + 1
            elif target < nums[mid]: #target smaller than mid, iugnore higher half
                hi = mid-1
        return -1
            
        