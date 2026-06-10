class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make nums a set
        # longest = 0
        # loop through set
            
            # check if num is a start of a sequence
                #yes, start sequence
                    # increment by 1 and increment length 
                    # length = 0
                #no, skip
        # return longest


        numsSet = set(nums)
        longest = 0

        for num in nums:
            
            if (num-1) not in numsSet:
                length = 0
                val = num
                while val in numsSet:
                    length += 1
                    val += 1
                if length > longest:
                    longest = length
        
        return longest
        







        