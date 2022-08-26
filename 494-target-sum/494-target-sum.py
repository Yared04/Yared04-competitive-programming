class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def rec(idx, tot):
            if tot == target and idx > len(nums)-1:
                return 1
            if idx >= len(nums) : return 0
            
            return rec(idx+1, tot + nums[idx]) + rec(idx+1, tot + -nums[idx])
        return rec(0, 0)
            
                 