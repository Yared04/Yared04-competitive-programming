def insertionSort1(n, arr):
    for i in range(n-1,-1,-1): 
         var = arr[i]
         for j in range(i-1,-1,-1):
           if arr[j] > var:
                arr[j+1] =arr[j]
           elif  arr[j] < var:
                arr[j+1] = var
            
           print(*arr)
         break
                       
    
one = [1, 3, 5, 9 ,13, 22, 27, 35, 46, 51, 55, 83, 87, 23]
on = [2,4,6,8,3]
insertionSort1(14,one)


# print(ar.count(2))
