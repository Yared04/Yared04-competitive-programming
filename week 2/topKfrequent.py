def topKFrequent(nums, k):
    new = dict()
    count=[]
    for i in range(len(nums)):
        if nums[i] not in new:
            new[nums[i]] = 1
        else:
            new[nums[i]] += 1
    print(new)
    for num in new:
        count.append(new[num])   
    count.sort(reverse=True)
    output = []
    for val, num in new.items():
        for value in count[:k]:
            if num == value:
                set(output.append(val))
    return list(output)
                
nums = [1,2]
k = 2
print(topKFrequent(nums,k))