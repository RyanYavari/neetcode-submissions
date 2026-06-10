'''
Pseudocode:
- In an array, return i and j such that nums[i] + nums[j] == target and i != j
if (nums[i] + nums[j] == target) AND i != j:
    return [i,j]

make a hashmap called "seen"
loop i through nums
complement = target - i
if complement is in seen:


'''
'''
Notes:

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, value in enumerate(nums):
            complement = target - value
            if(complement in seen):
                return [seen[complement], i]
            seen[value] = i
        


