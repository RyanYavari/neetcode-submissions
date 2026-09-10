class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''

        Input: nums = [3,4,5,6,1,2], target = 1

        Output: 4


        edge caes:
        empty array
        single array
        regular array
        different kinds of regular arrays


        return index of target within nums, or -1 if not present
        return nums[4]

        all elements are unique -> set? 

        Do it in O(logn) times

        O(logn) -> binary search

        1. unsort the array (we need sorted arr for binary search)
        2. perform binary search finding target 1
        3. return original index of that num 

        the array is sorted in 2 halfs

        target = 1
        3   4   5   6   1   2     
                    l   m   r
        
        1   2   3   4   5   6


        while l <= r:
            mid = (left + right)//2

            if target == mid:
                return index of target
            if target < m and target < l -> target must be on the right
                l = mid + 1
            if target < m and target > l -> target must be on the left of mid
                right = mid - 1
            if target > m and target > l -> target must be on right
                left + 1 
        
        return -1


        # array is sorted
        1, 2, 3, 4, 5, 6 
        l
        m
        r    

        #rotated, target on right
        3, 4, 5, 6, 1, 2

        # rotated, target on left
        6, 1, 2, 3, 4, 5, target = 1

        l = 6
        m = 2
        r = 5  

        # rotated, target at mid
        5, 6, 1, 2, 3, 4
        '''





        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if target == nums[mid]:
                return mid

            # if left <= mid, left side is a sorted array
            if nums[left] <= nums[mid]:
                
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1


            # if right >= mid,  right side is a sorted array
            
            if nums[right] >= nums[mid]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

        