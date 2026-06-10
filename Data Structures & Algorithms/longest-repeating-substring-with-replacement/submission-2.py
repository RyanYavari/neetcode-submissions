class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count {}
        # l, res = 0, 0
        # for r in range (len(s))
            # increment the hashmap count for the current char 

            # while violating the condition: window size - max frequency of char in window > k
                # shift the left of the window until the condition isnt violated
                    # remove the char from count
                    # l++
            # now that the condition isn't violated, calculate for max length of window

        count= {}
        l, res = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        
        return res

        
            
        