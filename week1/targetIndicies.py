def targetIndices(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[i],nums[j]= nums[j],nums[i]
    for i in range(len(nums)):
        if nums[i] == target:
            output.append(i)
    return output
arr=[1,3,2,2,5]   
n=len(arr)                
print(targetIndices(arr,4))




