class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return 
        

    def pop(self) -> None:
        self.stack.pop()
        return
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        for i in range(len(self.stack)):
            mini = self.stack[0]
            if self.stack[i] < mini:
                mini = self.stack[i]
            return mini
    

obj = MinStack()
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()