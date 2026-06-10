class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = [[] for i in range(len(nums) + 1)]
        # count = {} num: frequency
            # loop through nums to build hashmap
        # bucket sort
            # index is the frequency of the number
            # value is the list of numbers of that frequency
        # return top k
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items(): # count.items = ((2,3), (3,2), etc)
            freq[c].append(n)
        
        result = []
        for num in range(len(freq) - 1, 0, -1):
            for val in freq[num]:
                result.append(val)
                if len(result) == k:
                    return result

        
        


        
      

