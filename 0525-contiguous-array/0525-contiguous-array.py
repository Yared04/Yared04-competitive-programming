class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum= 0
        ans = 0
        idx_map = defaultdict(list)
        idx_map[0] = 0
        for i,num in enumerate(nums):
            prefix_sum += -1 if num == 0 else 1
            if prefix_sum in idx_map:
                ans = max(ans, i + 1 - idx_map[prefix_sum])
            else:
                idx_map[prefix_sum] = i + 1
                
        return ans
        