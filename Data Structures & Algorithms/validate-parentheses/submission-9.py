class Solution:
    def isValid(self, s: str) -> bool:

        '''

        closeToOpen = {'}': '{', ')': '(', ']': '['}
        stack = []

        loop through each char in s:
            if char is closing parenthesis: 
                if stack and stack[-1] == closeToOpen(char): #were checking to see if the last char in stack is a open paranthesis to the current closing paranthesis
                    stack.pop() 
                else:
                    return False
            else: #if char is opening parenthesis
                add char to stack

        return True if not stack else False #only return true if the stack is empty, meaning all open parenthesis were closed
                
        '''

        closeToOpen = {'}': '{', ')': '(', ']': '['}
        stack = []

        for c in s:
            if c in closeToOpen: #if c is a closing parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: #if c is opening parenthesis
                stack.append(c)
    
        return True if not stack else False




        
        