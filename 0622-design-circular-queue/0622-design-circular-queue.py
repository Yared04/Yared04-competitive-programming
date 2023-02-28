class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.size = 0
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.head == -1:
            self.head += 1
        
        self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail] = value
        self.size += 1
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        
        return True
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.data[self.head]
        
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.data[self.tail]
        
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()