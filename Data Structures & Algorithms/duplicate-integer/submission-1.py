class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a array values 
        # loop through array and check if nums[i] is in values
            # if nums[i] is in values, return true
            #else, append nums[i] to values
        # return false

        values = []
        for i in range(len(nums)):
            if nums[i] in values:
                return True
            else:
                values.append(nums[i])
        return False

        