def minSetSize(arr) -> int:
    new = dict()
    output=[]
    size = len(arr)//2
    for i in range(len(arr)):
        if arr[i] not in new:
            new[arr[i]]=1
        elif arr[i] in new:
            new[arr[i]] += 1
    print(new)
    for num in new:
        output.append(new[num])
    output.sort(reverse=True)
    sum = 0
    count = 0
    for i in range(len(output)):
       if sum < size:
             sum += output[i]
             count += 1
    return count
                     
          
arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
# print(arr.count(3))
print(minSetSize(arr))