class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        # Main idea: Find out which side is sorted. If the left side is sorted, minimum cant be there, search right half.
        If the right side is sorted, the minimum must be in the left or in the middle, search left half.

        1. Initialize l and r, and minimum = first number in array (doesnt matter what num in array)

        while l <= r:
            a. if nums[l] is less than nums[r], the arr is sorted. break
            b. compute mid
            c. run min(minimum, nums[mid])
            d. Find which side is sorted 
                if mid >= left: We know left is sorted, search right
                    l = mid + 1
                else: We know right is sorted, search left
                    r = mid - 1
        
        return minimum

        '''
        minimum = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])
            
            if nums[mid] >= nums[l]: #Left side is sorted, search right
                l = mid + 1
            else:
                r = mid - 1
        
        return minimum



        