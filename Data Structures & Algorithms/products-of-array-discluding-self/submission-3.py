class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        '''
        1. calculate prefix in output
        sum of every number in nums before index i -> output[i] = sum 

        2. calculate postfix in output
        sum of every number in nums after index i -> output[i] *= sum (multiply prefix and postfix)

        return output



        '''
        n = len(nums)
        output = [1]*n
        prefix, postfix = 1, 1

        # prefix
        for i in range(n):
            if i == 0:
                prefix *= nums[i]
            else:
                output[i] = prefix
                prefix *= nums[i]
        
        #postfix

        for i in range(n-1, -1, -1):
            if i == n-1:
                postfix *= nums[i]
            else:
                output[i] *= postfix
                postfix *= nums[i]
        
        return output

        





        
        