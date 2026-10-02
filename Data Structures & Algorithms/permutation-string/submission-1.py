class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        '''
        checking to see if substring exists -> sliding window

        get freq hashmap of s1

        loop through s2 
            g
            get a hashmap of a fixed window size of len(s1) 
            compare the hashmap to freq hashmap of s1
                if equal, return true
        
        return false


        '''

        # freq hashmap of s1

        s1freq = {}
        for c in s1:
            s1freq[c] = s1freq.get(c, 0) + 1
        
        #loop through s2


        l, r = 0, 0

        while r < len(s2):

            r = l
            freq = {}

            # compute hashmap of fixed length s1 
            while (r-l+1) <= len(s1) and r < len(s2):
                freq[s2[r]] = freq.get(s2[r], 0) + 1
                r += 1
            
            if freq == s1freq:
                return True

            l += 1
        
        return False
            










