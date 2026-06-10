class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # traverse through an array with two pointers on opposite ends, left pointer and right pointer
        # check to see if numbers[left] + numbers[right] == target
            # if yes, return [left, right]
            # if no and numbers[left] + numbers[right] < target, increment left
            # if no and numbers[left] + numbers[right] > target, decrease right
            # do this while left < right
        
        left = 0
        right = len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        
        return [left+1, right+1]

