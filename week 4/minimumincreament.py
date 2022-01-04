class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1] += 1
                count += 1
            elif nums[i] > nums[i+1]:
                k = (nums[i]+1) -nums[i+1]
                nums[i+1] += k
                count += k
                   
        print(nums)
        return count
                