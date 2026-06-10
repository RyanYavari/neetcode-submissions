class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hashmap {} where strings s and t have their character as the key and frequency as value
        # compare key and value pair
            # return false if not same pair
        # return true
        # edge case: check if strings are same length

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True

