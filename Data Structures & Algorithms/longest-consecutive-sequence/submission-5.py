class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        # start of a sequence -> num-1 is not in numSet

        1. find start of sequence
        2. start counting in a while loop where you increment count and val until val doesnt exist in numSet


        '''


        numSet = set(nums)
        maxSequence = 0


        for num in nums:
            if (num-1) not in numSet:
                val = num
                count = 1

                while val+1 in numSet:
                    count += 1
                    val += 1
                
                maxSequence = max(maxSequence,count)
        
        return maxSequence

        
            
        