class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(nums)
        nums = list(set_nums)
        nums.sort(reverse=True)
        return nums[2]