class Solution:
    def isValid(self, s: str) -> bool:

        '''

        closeToOpen = {'}': '{', ')': '(', ']': '['}


        


        '''

        closeToOpen = {'}': '{', ')': '(', ']': '['}

        stack = []

        for c in s:
            if c in closeToOpen: #if closing parenthesis
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: #if not closing parenthesis, add the open parenthesis to the stack
                stack.append(c)
        
        return True if not stack else False


        