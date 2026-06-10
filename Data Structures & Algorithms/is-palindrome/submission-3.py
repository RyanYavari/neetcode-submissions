class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string to be case-insensitive and ignore non-alphanumerics
        # s = s.lower()
        # for c in s:
            # if c.isalnum()
                # append c to cleanStr
        # return cleanStr == cleanStr[::1]

        s = s.lower()
        cleanStr = ""
        for c in s:
            if c.isalnum():
                cleanStr += c
        return cleanStr == cleanStr[::-1]
        