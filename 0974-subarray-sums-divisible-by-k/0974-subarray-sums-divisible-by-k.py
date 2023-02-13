class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        ans = prefix_sum = 0
        for i,num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k
            if rem < 0:
                rem += k
            if rem in freq:
                ans += freq[rem]
                freq[rem] += 1
            else:
                freq[rem] = 1
        return ans
        