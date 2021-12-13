class Solution: 
    def select(self, arr, i):
        # code here
        startIdx = i
        minval = arr[i]
        for idx, val in enumerate(arr[i:]):
            if val < minval:
                startidx = idx + 1
                minval = val
        return startIdx
            
        
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            for j in range(i+1,n):
                if arr[j] < arr[i]:
                    arr[i],arr[j]= arr[j],arr[i]