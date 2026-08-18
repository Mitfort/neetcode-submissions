class MinStack:

    def __init__(self):
        self.data = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.data.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
