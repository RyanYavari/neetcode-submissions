'''
Notes:
- str.lower() converts all characters in a string to lowercase
- str.replace(" ", "") removes all spaces in a str
- Cannot do str.remove(), .remove() only works for lists
- .isalnum() checks if any character is a letter or number
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:

        
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
            
    
