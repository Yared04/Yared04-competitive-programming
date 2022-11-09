class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = [0]
        idx_map = defaultdict(list)
        for num in nums:
            if num == 0:
                prefix_sum.append(prefix_sum[-1] + -1)
            else:
                prefix_sum.append(prefix_sum[-1] + 1)
        
        for i,s in enumerate(prefix_sum):
            idx_map[s].append(i)
        
        ans = 0
        for key, val in idx_map.items():
            if len(val) > 1:
                ans = max(ans, val[-1] - val[0])
        return ans
        