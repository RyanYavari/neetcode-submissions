class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        print(s)
        # Convert string to all lowercase 
        s = s.lower()
        #Convert string to have no spaces
        s = s.replace(" ", "")
        #Remove non alpha numerics
        result = ''
        for char in s:
            if char.isalnum():
                result += char
        
        #Check if palindrome
        reverse = result[::-1]
        if result == reverse:
            return True
        
        return False
            
    
