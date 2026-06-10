class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashSet = set()
        l = 0
        maxSize = 0
        
        for r in range(len(s)):
            char = s[r]
            while char in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(char)
            maxSize = max(maxSize, len(hashSet))
        
        return maxSize

        
        