class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        '''
        
        1. sort nums

        2. for i in range(len(nums)):
                l, r = i+1, len(nums)-1
                if sum of i, l, r > 0: # sum is too large, r--
                elif sum of i, l, r < 0: #sum is too small, l++
                else: #they sum to 0, add to output
                


        '''
        output = []

        nums.sort()

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            
            l, r = i+1, len(nums)-1

            while l < r:
                if (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return output


        '''
        nums = [-4, -1, -1, 0, 1, 2]
                        i   l     r    

        output: [[-1, -1, 2], [-1, 0, 1]]

        '''
        
