class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''

        output = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperates):

            while stack and the top of the stack's temp < temp:
                stackI, stackT = stack.pop() # pop and decouple tuple
                output[stackI] = idx-stackI
            stack.append((idx, temp))
        
        return output

        '''

        output = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, stackI = stack.pop()
                output[stackI] = idx-stackI
            stack.append((temp,idx))
        
        return output


        '''
Input: temperatures = [30,38,30,36,35,40,28]
                                         i 
stack = 40, 28
Output: [1, 4, 1, 2, 1, 0, 0]


        


        '''

        