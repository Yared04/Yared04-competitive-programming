class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        j = 0
        while j < len(nums):
            zeros = 0
            while j < len(nums) and nums[j] == 0:
                j += 1
                zeros += 1
                count += zeros
            j += 1
        return count
            
            