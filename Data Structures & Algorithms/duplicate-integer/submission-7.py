class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''

        hash set -> checks for duplicates

        loop through arr
            check if val in set
                if in set, return true
            else, 
                add to set
        
        return false

        Time complexity: o(n)


        '''
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False
        