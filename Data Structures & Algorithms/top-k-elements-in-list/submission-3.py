class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        '''

        1. calcualate frequencies of each integer in nums -> hashmaps
        2. populate our bucket where index is frequency count, value is the integer in nums
            frequency of 2: 2
        3. sweep values from end of bucket until output arr length is == k
        

        '''

        output = []

        #populate frequency hashmap
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # populate bucket, we do len(nums)+1 because we are creating a frequency range, and frequencies start from 1 not 0
        bucket = [[] for _ in range(len(nums)+1)]

        for key, count in freq.items():
            bucket[count].append(key)
        
        # sweep values from end of bucket until output arr is len k
        
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                output.append(j)
                if len(output) == k:
                    return output

        


        

        