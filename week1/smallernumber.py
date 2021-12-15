def smallerNumbersThanCurrent(nums):
    
    count=[0]*len(nums)
    for i in range(len(nums)):
        ctr =0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                ctr += 1
                count[i]=ctr
    return count
                
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
            
    
    