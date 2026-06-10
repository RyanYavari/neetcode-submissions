class Solution:
    def isValid(self, s: str) -> bool:

        # stack = []
        # for c in s
            # if c is a closing parenthesis
                # if stack not empty and end of stack is equal to c's opening parenthesis
                    # stack.pop()
                # else
                    # return False
            # if c is an opening parenthesis
                # stack.append(c)
        #return True if stack is empty, False if its not

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False



        