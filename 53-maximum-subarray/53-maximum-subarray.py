class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dp(idx, pick):
            if idx >= len(nums): return 0 if pick else -inf
            if pick:
                return max(nums[idx]+dp(idx+1, True),0)
            return max(nums[idx] + dp(idx+1, True), dp(idx+1, False))
        return dp(0, False)