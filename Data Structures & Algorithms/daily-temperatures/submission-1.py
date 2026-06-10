class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''

        res = [0]*n
        stack = [] # holds tuples of (temp, index)

        loop i, temp through temperatures:
            
            while stack and stack[-1] < temp:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((temp, i))
        
        return res
            

        '''
        res = [0]*len(temperatures)
        stack = [] # holds tuples of (temp, index)

        for i, temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((temp, i))
        
        return res



        


        