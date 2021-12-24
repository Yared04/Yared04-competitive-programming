class MyQueue:

    def __init__(self):
        self.stak1 = []   
        self.stak2 = []   

    def push(self, x: int) -> None:
        self.stak1.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        elif len(self.stak2) == 0 and len(self.stak1) > 0:
            while len(self.stak1):
                temp = self.stak1.pop()
                self.stak2.append(temp)
            return self.stak2.pop()
 
        else:
            return self.stak2.pop()
        

    def peek(self) -> int:
        if not self.empty():
            return self.stak2[0]
        

    def empty(self) -> bool:
        if len(self.stak1) == 0: 
            return True
        return False
        
obj = MyQueue()
obj.push(3)
obj.push(89)
obj.push(90)
print(obj.pop())
print(obj.pop())
print(obj.empty())
