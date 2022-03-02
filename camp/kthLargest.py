import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums 
        self.k = k
        self.arr = []
        for i in range(self.k):
            if self.k > len(self.nums)+1 or i > len(nums)-1 :
                break
            self.arr.append(self.nums[i])
        print(self.arr)
        heapq.heapify(self.arr)
        for i in range(self.k, len(self.nums)):
            if self.arr[0] < self.nums[i]:
                self.arr[0] = self.nums[i]
                heapq.heapify(self.arr)
        
        

    def add(self, val: int) -> int:
        if self.arr:
            if len(self.arr) < self.k:
                self.arr.append(val)
                heapq.heapify(self.arr)
            elif val > self.arr[0]:
                self.arr[0] = val
                heapq.heapify(self.arr)
            elif val < self.arr[0] and len(self.arr) < self.k:
                self.arr.append(val)
                heapq.heapify(self.arr)
                print(self.arr)
           
        else:
            self.arr.append(val)
        return self.arr[0]
            
            
        
        
       
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)