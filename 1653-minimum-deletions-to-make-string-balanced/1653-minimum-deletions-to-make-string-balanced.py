class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0
        dp = [0] * len(s)
        for idx, char in enumerate(s):
            if char == "a":
                dp[idx] = min(count_b, dp[idx-1] + 1)
            else:
                count_b += 1
                dp[idx] = dp[idx - 1]
        return dp[-1]
        