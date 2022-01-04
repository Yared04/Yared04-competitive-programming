def insertionSort1(n, arr):

   var = arr[-1]      
   j = n - 2
   while arr[j] > var and j > -1:
                arr[j+1] = arr[j]
                j -= 1
                print(*arr)
   arr[j+1] = var       
   print(*arr)  
                
    
one = [2,3,4,5,6,7,8,9,10,1]
on = [2,4,6,8,3]
insertionSort1(10,one)


# print(ar.count(2))
