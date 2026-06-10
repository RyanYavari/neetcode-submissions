class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''

        * we know arr is sorted in increasing order and wants two indices returned -> two pointers
        * return indexes, not values
        * must use O(1) space -> two pointers

        l, r = 0, len(numbers)-1
        
        while l < r:
            if sum of values at l and r > target, reduce r (we know that reducing r reduces the sum since the arr is sorted)
                r -= 1
            if sum of values at l and r < target, increase l (we know that increasing l increases the sum since the arr is sorted)
                l -= 1
            if sum of values = target
                return [l+1, r+1]
        
            


        '''

        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] < target:
                    l += 1
            elif numbers[l] + numbers[r] > target:
                    r -= 1    
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]
        
        '''
        dry run: 
        Input: numbers = [1,2,3,4], target = 3

        l = 0
        r = 3, 2, 1




        '''
        