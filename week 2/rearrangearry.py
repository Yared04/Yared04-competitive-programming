def rearrangeArray(nums):
  while True:
            count = 0
            for i in range(1, len(nums)-1):
                 if nums[i] == (nums[i-1] + nums[i+1])/2:
                         nums[i-1], nums[i] = nums[i],nums[i-1]
                         count +=1
            if count == 0:
                break
  return nums

print(rearrangeArray([10,7,5,4,3]))