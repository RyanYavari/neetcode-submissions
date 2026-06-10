class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        On^2 time, O(1) space

        * indices all must be distinct
        * any order
        * no duplicate triplets


        return certain # of indices -> pointers (3 pointers)
        return distinct triplets -> List of lists

        result = [[]] # returning list of lists

        nums.sort() # sort the arr

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1

            while j < k:
                if sum > 0:
                    k--
                elif sum < 0:
                    j++
                elif sum == 0:
                    result.append([nums[i], nums[j], nums[k])
                    either increase j or decrease k
        
        return result


        '''

        result = []
        nums.sort()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                elif total == 0:
                    result.append([nums[i], nums[j], nums[k]]) 
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return result
        


        