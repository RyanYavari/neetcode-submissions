class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''

        sorted array, finding two indexes -> two pointers

        l = 0, r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target: #sum bigger than target, reduce r 
                r--
            elif numbers[l] + numbers[r] < target: #sum smaller than target, increase l
                l++
            else: # sum == target, return both indexes (1-indexed)

        '''

        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target: 
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                return [l+1, r+1]
        