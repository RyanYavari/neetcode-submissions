class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        '''

        return 2 indices that sum to target

        visited = {}
        
        for index, num in nums:
            diff = target - num
            if diff in visited # if diff has been visited before, we found our pair that sum up to target. return the indice of diff
                return [visited[diff], index]
            visited[num] = index # add num and index to visited set
        return


        '''

        visited = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], index]
            visited[num] = index
        
        return


        