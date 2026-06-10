class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return arrays of triplets
        # cannot contain duplicates
        # can be in any order

    # solution in O(n^2) time and O(1) space:
        # sort array
        # for i in range(len(nums)-1):
            # j = 0, k = n - 1
            # while j < k
                # if nums[i] + nums[j] + nums[k] < 0:
                    # j += 1
                # if nums[i] + nums[j] + nums[k] > 0:
                    # k -= 1
                # if nums[i] + nums[j] + nums[k] == 0:
                    # append to result    
        # return result

        result = []

        nums.sort()

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            
            while j < k:

                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return result


