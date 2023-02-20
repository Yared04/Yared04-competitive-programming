class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        _max= -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    _max = max(_max, nums[j] - nums[i])
        return _max
        
        