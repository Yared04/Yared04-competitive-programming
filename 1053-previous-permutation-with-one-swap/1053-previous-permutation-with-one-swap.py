class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        '''
        [1,4,9,6,7] => [1,4,7,6,9]
        [1,4,9,6,7,3] =>  [1,4,9,6,3,7]
        [1,4,4,7,6,9] => [1,4,4,6,7,9] 
        [1,4,7,6,4,9,5] => [1,4,7,4,6,5,9]
        
        [(9,5), (7,3), (6,4) ... (1,0)]
        [(9,2),(7,4),(6,3),(4,1),(3,5)(1,0)]
        
        '''
        num1 = 0
        num2 = (0, 0)
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                num1 = i
                break
        for j in range(num1+1,len(arr)):
            if arr[num1] > arr[j]:
                if num2[0] < arr[j]:
                    num2 = arr[j], j
        arr[num1], arr[num2[1]] = arr[num2[1]], arr[num1]
        return arr
                
                
            
            