class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = [] #the minimum number is always on the top of the stack 
        
   

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
                
        


        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        
        return self.min_stack[-1]



        
