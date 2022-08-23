class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses):
            dp1, dp2 = 0, 0
            for i in range(len(houses)):
                dp1, dp2 = max(dp2+houses[i], dp1), dp1
            return dp1
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
        