class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''

        window = set()
        longest = 0
        l, r = 0

        for c in s:
            while c is in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            longest = max(longest, len(window))

        return longest

        dry run:

        z   x   y   z   x   y   z
                l
                            c

        longest=3
        window=yzx

        '''

        window = set()
        longest = 0
        l = 0

        for c in s:
            while c in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            longest = max(longest, len(window))

        return longest


        