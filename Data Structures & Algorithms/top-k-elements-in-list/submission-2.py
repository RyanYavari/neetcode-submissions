class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        1. get freq of each element via hashmap
        
        2. bucket sort 

            bucket[freq] = values
            bucket is size of nums arr
        
        3. sweep from end of arr until output size reaches k


        '''
        n = len(nums)

        # get freq of each element via hashmap
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket = [[] for _ in range(n+1)]

        #bucket sort
        for key, count in freq.items():
            bucket[count].append(key) 
        
        # sweep values from end of bucket until output size = k
        output = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                output.append(j)
                if len(output) == k:
                    return output
        






        

        
        
    

        
            







        
