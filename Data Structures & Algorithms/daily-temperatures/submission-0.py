class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # stack = []
        # res = []
        # go through temperatures array and add element to stack
            # at top of stack, check if there are values less than top of stack
                # if there are, then find right - left & add to res, then remove right
            
        
        stack = []
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t, i))
        return res
                





            

                
        