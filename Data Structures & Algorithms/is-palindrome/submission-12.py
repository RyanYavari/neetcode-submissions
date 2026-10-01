class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''

        palindrome -> two pointer 

        ignore non alphanumeric characters -> str.isalnum() python built in function

        l, r = 0, len(s)-1

        1. while l < r:
            1.1 while l < r and l is not alnum:
                l++
            1.2 while l < r and r is not alnum:
                r++
            # at this point, both l and r are alnum, so compare
            if s[l] != s[r]:
                return False #not a palindrome
            # else, if they are then increment l and decrement r
            l++
            r--       
        
        2. return True # at this point, the string is confirmed to be a palindrome if False was never called

        '''

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]): #increment l until it is alnum
                l += 1
            while l < r and not self.isAlphaNum(s[r]): # decrement r until it is alnum
                r -= 1
            
            #now that both pointers are alnum, compare the LOWER case characters
            if s[l].lower() != s[r].lower(): 
                return False
            
            #increment l, decrement r
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        )










