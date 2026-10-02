class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        '''

        windowLen - count[most freq character] <= k

        

        count = {}
        l = 0
        longest = 0
        maxF = 0

        '''


        count = {}
        l = 0
        maxWindowLen = 0
        maxF = 0


        for r in range(len(s)):
            
            #calculate max frequency in window
            count[s[r]] = count.get(s[r], 0)+1
            maxF = max(maxF, count[s[r]])

            #while window is invalid, increment l
            while (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            #now that window is valid, calculate result
                # result = length of window (r-l+1)
            
            maxWindowLen = max(maxWindowLen, r-l+1)
        
        return maxWindowLen

            
            
            
            
            
            
            
            
