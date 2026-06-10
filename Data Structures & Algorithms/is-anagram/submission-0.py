class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d_s = {}
        d_t = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in d_s:
                d_s[i] += 1
            else:
                d_s[i] = 1
        
        for i in t:
            if i in d_t:
                d_t[i] += 1
            else:
                d_t[i] = 1
        
        print(d_t)
        print(d_s)

        for key in d_t:

            if d_t[key] != d_s.get(key, 0):
                return False
        
        return True

        
        