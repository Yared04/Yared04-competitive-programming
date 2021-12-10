def goodpairs(nums):
    ctr = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]==nums[j] and i < j:
                ctr += 1
    print(ctr)
ar=[1,2,3]
goodpairs(ar)
                
    