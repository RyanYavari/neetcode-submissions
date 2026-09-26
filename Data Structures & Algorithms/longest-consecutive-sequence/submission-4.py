class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        '''

        start of sequence -> num-1 doesnt exist
        
        1. when you a find the start of a sequence
            run a while loop
                if num + 1 in numSet, increment
                log longest
        
        return longest




        '''

        numSet = set(nums)

        longestSequence = 0

        for num in nums:
            if (num-1) not in numSet: #we know its the start of a sequence
            
                val = num
                count = 1
                
                while (val+1) in numSet:
                    val += 1
                    count += 1
                
                longestSequence = max(longestSequence, count)

            

        
        return longestSequence
        