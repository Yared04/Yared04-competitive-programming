def maxOperations(nums, k):
    count= 0
    new = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums) ):
            # if nums
            # if nums[i] == 0 or nums[j]==0:
            #     continue
            if nums[i] +nums[j] == k and nums[i] != 0 and nums[j] != 0 :
                count+=1
                nums[i] = 0
                nums[j] = 0
    print(nums)
    return count
nums =[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
print(maxOperations(nums,2))
                