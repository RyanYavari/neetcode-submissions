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
        
        for num in count: # 2 : 2 times
            index = count.get(num)
            freq[index].append(num)
        
        freq.reverse()
        result = []
        for i in range(len(freq)):
            if len(result) < k and freq[i] != []:
                for val in freq[i]:
                    result.append(val)
        
        return result
        
        


        
      

