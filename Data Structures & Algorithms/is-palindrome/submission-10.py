class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''

        1. convert string to case insensitive and ignore non-alphanumeric characters
            use .isalnum() & .lower()
        
        2. Two pointer comparison starting from far left and then far right. Compare every character and move both pointers until they reach middle
            if char at both pointers not equal, return false
        
        return true if sucessfully passes loop
    

        '''

        

        l, r = 0, len(s)-1
  

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))







                

        