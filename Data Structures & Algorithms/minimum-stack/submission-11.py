class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:

        # if val is smaller than top of minStack, add it. if not, then dont add it

        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)
        


        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        #return the minimum element in stack in O(1)
        #min heap is log n to O(n) - X
        # min() function is O(n) - X
        # use a separate stack to hold the min val

        # minStack should have the smallest element at the top of the stack

        return self.minStack[-1]




        
