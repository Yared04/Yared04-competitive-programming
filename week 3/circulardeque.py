class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [] * k 
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque.insert(0, value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque.pop(0)
            return True
        return False
    
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop(-1)
            return True
        return False
          
    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        return False
    
    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[0]
        return -1       
        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[-1]
        return -1
                  

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        return False
