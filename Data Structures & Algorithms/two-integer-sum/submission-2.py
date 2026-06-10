'''
Pseudocode:
- In an array, return i and j such that nums[i] + nums[j] == target and i != j
if (nums[i] + nums[j] == target) AND i != j:
    return [i,j]

1. Make a hashmap called 'seen' that is value -> index
2. Enumerate through nums list: for i, value in enumerate(nums)
3. complement = target - value
4. If complement in hash map
    - We know that value + complement = target
    - Return indexes: [seen[complement], i]
5. If complement is not in hash map
    - seen[value] = i
6. Loop back to step 2


'''
'''
Notes:
1. Use hash map when looking through an array so that the run time is O(1) rather than looping to n and having a run time of O(n)
2. enumerate(item) function
- Syntax: for i, value in enumerate(nums):
- Use cases:
    A. When you need both the index and value in a loop


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, value in enumerate(nums):
            complement = target - value
            if(complement in seen):
                return [seen[complement], i]
            seen[value] = i
        


