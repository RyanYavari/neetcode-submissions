class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix, postfix = 1
        # output = []
        # prefix round
            # find the prefix for every number and compound to output array
            # find the postfix for every number and compound to the output array

        prefix, postfix = 1, 1
        output = [1]*len(nums)

        #prefix round
        for index, num in enumerate(nums):
            if index == 0:
                continue
            else:
                prefix *= nums[index-1]
                output[index] = output[index]*prefix
        
        #postfix round

        for index, num in reversed(list(enumerate(nums))):
            if index == len(nums)-1:
                continue
            else:
                postfix *= nums[index+1]
                output[index] = output[index]*postfix
        
        return output

            
        
            


            
        