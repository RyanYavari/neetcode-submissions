class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''

        1. convert string to case insensitive and ignore non-alphanumeric characters
            use .isalnum() & .lower()
        
        2. Two pointer comparison starting from far left and then far right. Compare every character and move both pointers until they reach middle
            if char at both pointers not equal, return false
        
        return true if sucessfully passes loop
    

        '''

        

        newS = ""
        for c in s:
            if self.isAlphaNum(c):
                newS += c.lower()
        
        l, r = 0, len(newS)-1
  

        while l < r:
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))







                

        