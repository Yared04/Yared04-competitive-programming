def minPairSum(nums) -> int:
    nums.sort()
    new =[]
    for i in range(len(nums)//2):
        for j in range(len(nums)-1-i,len(nums)//2-1,-1):
            new.append(nums[i]+nums[j])
            break
    return max(new)
    
nums =[3,5,2,3]
print(minPairSum(nums))