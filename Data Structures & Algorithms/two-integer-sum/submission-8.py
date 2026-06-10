class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''

        return indices (ordered placement in array) of two numbers that sum up to target
        
        Every input has one pair of indices that satisfy the condition

        Return answer with smaller index first

        List is unordered, so dont use 2 pointer 
        
        Solution:

        hashMap -> num : index of num from nums arr

        We are capitalizing on the characteristic of hash sets where "in" is an O(1) operation

        

        '''

        hashMap = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap.get(diff, 0), idx]
            else:
                hashMap[num] = idx
        
        return False