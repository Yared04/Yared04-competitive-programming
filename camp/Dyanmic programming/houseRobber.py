class Solution:
    def rob(self, nums: List[int]) -> int:
        max_loot = [0] * (len(nums)+2)
        max_loot[0] = nums[0]
        for i in range(1, len(nums)):
            max_loot[i] = nums[i] + max(max_loot[i-2], max_loot[i-3])
        return max(max_loot)