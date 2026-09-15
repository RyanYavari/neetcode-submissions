class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        sorted -> two pointers, binary search
        function searching for target -> binary search
        ologn time -> binary search 

            if mid < target:
                l = mid + 1
            elif mid > target:
                r = mid - 1
            else return mid
    
        return -1
        



        '''

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return -1

        