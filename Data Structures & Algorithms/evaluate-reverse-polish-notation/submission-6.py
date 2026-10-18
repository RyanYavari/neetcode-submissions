class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''

        loop through tokens

            number, append to stack
            if its an operator and there are 2 or more values in stack, pop the 2 values and perform operation, then add to stack




        '''

        operators = {'+', '-', '*', '/'}
        stack = []
        total = 0


        for i in tokens:
            if i in operators and len(stack) >= 2: #if i is an operator and stack has numbers
                val1 = stack.pop()
                val2 = stack.pop()
                if i == '+':
                    stack.append(int(val1+val2))
                elif i == '*':

                    stack.append(int(val1*val2))   
                elif i == '/':
   
                    stack.append(int(val2/val1))
                elif i == '-':
                    
                    stack.append(int(val2-val1))
                    
            elif i not in operators:
                stack.append(int(i))
        
        return stack[-1]

        