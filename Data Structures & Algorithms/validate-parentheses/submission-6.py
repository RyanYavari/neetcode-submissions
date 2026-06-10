class Solution:
    def isValid(self, s: str) -> bool:

        '''
        hashMap = {')': '(', '}': '{', ']': '['}

        stack = []

        * The last open parantheses must be the first one to close. Last in first out 

        loop through str
            check if its a closed parantheses
                if closed parantheses and last item in stack contains open parantheses
                    remove item from stack
                        # this process is ensuring that the first closed paranthesis is also the most recent open parantheses
                else: # this means that the last open paranthesis is NOT the first closed paranthesis, meaning its invalid as its not in order
                    return False
            if not a closed parantheses, its open and needs to be added to the stack
        
        return True if stack is empty and false if its not
        '''

        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in closeToOpen: #its a closed paranthesis
                if stack and stack[-1] == closeToOpen[c]: # if closed paranthesis matches the last item in stack (last open parantehsis)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False





        


        