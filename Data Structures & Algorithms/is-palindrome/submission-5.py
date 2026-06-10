class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1
        s = s.lower()

        while left < right:
            
            while left < right and self.alphaNum(s[left]) is False:
                left += 1
            while right > left and self.alphaNum(s[right]) is False:
                right -= 1
            
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True




    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
                
        

        