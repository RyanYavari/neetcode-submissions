class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        '''
        - use a hash set to count for duplicates
        - if there is a duplicate, return True. Else, return false

        pseudo:

        hashSet = set()
        loop through nums arr
            if num is in set, return true
            else, add num to set
        return false

        '''


        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        
        return False
        