def closestNumbers(arr):
    output = [ ]
    dic = {}
    arr.sort()
    for i in range(len(arr)-1):
        dif = arr[i+1] - arr[i]
        dic[arr[i], arr[i+1]] = dif
    mini = min(dic.values())
    for key, val in dic.items():
        if val == mini:
            output.append(key[0])
            output.append(key[1])
    print(dic)
    return output
arr= [-20, -3916237 ,-357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594 ,266854 ]
print(closestNumbers(arr))