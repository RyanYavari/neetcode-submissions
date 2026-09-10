class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''

        count = {} # hashmap with frequencies for each char

        l = 0
        res = 0
        window = ""

        for r in range(len(s)):
            add s[r] to window
            
            check if window - maxFreq <= k:
            res = max(r - l + 1, res)
            else:
                while the following condition is false window - maxFreq <= k 
                    reduce count of char at s[l]
                    l+= 1
        
        return res


        '''

        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

            res = max((r-l+1), res)
        
        return res

            

            
        