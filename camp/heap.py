import heapq

#User function Template for python3

class Solution:
       
        def leftChild(self, i, arr):
            if i < (len(arr)//2):
                return (2*i)+1
            else:
                return None

        def rightChild(self, i, arr):
            if len(arr)%2 != 0 and i < ((len(arr)//2)):
               return (2*i)+2
            elif len(arr)%2 == 0 and  i < (len(arr)//2) - 1:
                return (2*i)+2
            else:
                return None
        def parent(self, i, arr):
            if i != 0:
                return (i-1)//2 
            else:
                return None
        def swap(self,idx1, idx2, arr):
            temp  = arr[idx1]
            arr[idx1] = arr[idx2]
            arr[idx2] = temp
        def getMin(self, arr):
            return arr[0]

        def insert(self, arr, val):
            arr.append(val)
            self.upHeap(arr, len(arr)-1)
        def update(self, arr, i, n , val):
            arr[i] = val
            self.heapify(arr, i,n)
        def remove(self, arr, i, n):
            if i != len(arr)-1:
                self.swap(i, len(arr)-1, arr)
            self.heapify(arr, i, n)
        def heapify(self, arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
              largest = l
            if r < n and arr[largest] < arr[r]:
              largest = r
            if largest != i:
              arr[i], arr[largest] = arr[largest], arr[i]
              self.heapify(arr, n, largest)
          
  
            
        def upHeap(self, arr, i):
            if self.parent(i,arr) != None and arr[i] < arr[self.parent(i,arr)]:
                # print(self.parent(i,arr))
                self.swap(i,self.parent(i,arr),arr)
                self.upHeap(arr, self.parent(i,arr))
            
        def downHeap(self, arr, i, n):
            if self.rightChild(i,arr)  and  arr[i] > arr[self.rightChild(i,arr)] and arr[self.leftChild(i,arr)] > arr[self.rightChild(i,arr)] and self.rightChild(i, arr) < n:
                self.swap(i, self.rightChild(i,arr),arr)
                self.downHeap(arr, self.rightChild(i,arr), n)
            elif self.leftChild(i,arr) and arr[i] > arr[self.leftChild(i,arr)] and self.leftChild(i,arr) < n:
                self.swap(i, self.leftChild(i,arr),arr)
                self.downHeap(arr, self.leftChild(i,arr), n)
          
        def buildHeap(self, arr):
            for elt in range(len(arr)):
                self.upHeap(arr,elt)
        def HeapSort(self, arr, n):
          
            n = len(arr)
            for i in range(n//2, -1, -1):
                  self.heapify(arr, n, i)
            for i in range(n-1, 0, -1):
                  arr[i], arr[0] = arr[0], arr[i]
                  self.heapify(arr, i, 0)
                     
          
                
            


one = Solution()
arr = [1,2,3,4,5,6,7]
one.heapSort([4,0,1,9,8,5,6,7,4,3,2,4,200,6], 14)
# print(one.rightChild(2,arr))
# print(one.parent(1,arr))
# print(one.swap(0,5,arr))
# print(arr)
# print(one.swap(0,5,arr))
# one.upHeap(arr,7)
# print(one.leftChild(7,arr))
# print(one.rightChild(7,arr))
# print(one.parent(3,arr))
# one.downHeap(arr,3)
# one.insert(arr,9)
# one.insert(arr,2)
# one.remove(arr,3)

# one.update(arr,0,0)  

# print(arr)
