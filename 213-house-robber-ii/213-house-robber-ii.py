class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses):
            dp = [0] * (len(houses)+2)
            dp[0] = houses[0]
            for i in range(1,len(houses)):
                dp[i] = houses[i] + max(dp[i-2], dp[i-3])
            return max(dp)
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
        