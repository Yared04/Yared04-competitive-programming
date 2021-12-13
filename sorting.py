def insertionSort1(n, arr):
    for i in range(1,n): 
         for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                var = arr[j]
                arr[j] =arr[j + 1]
                arr[j+1] = var
            
            print(*arr)
                       
    
one = [1, 3, 5, 9 ,13, 22, 27, 35, 46, 51, 55, 83, 87, 23]
# insertionSort1(14,one)


# print(ar.count(2))
