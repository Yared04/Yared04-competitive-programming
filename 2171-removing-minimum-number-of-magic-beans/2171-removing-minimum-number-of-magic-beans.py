class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix_sum = [beans[0]]
        for i in range(1,len(beans)):
            prefix_sum.append(prefix_sum[-1] + beans[i])
        print(prefix_sum)
        ans = (prefix_sum[-1] - prefix_sum[0]) - beans[0] * (len(beans)-1)
        print(ans)
        for i in range(1, len(beans)):
            ans = min(ans, (prefix_sum[-1] - prefix_sum[i]) - beans[i] * (len(beans)-i-1) + prefix_sum[i-1])
        return ans

