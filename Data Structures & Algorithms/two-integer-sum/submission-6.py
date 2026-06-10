class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap with key: number & value: index of number
        # Loop through the nums array 
            # Check if target-number is in hashmap
                # if not, add number to hashmap and continue
                # if yes, return current number index and the target-number index
        
        hashmap = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[num] = index
        return
