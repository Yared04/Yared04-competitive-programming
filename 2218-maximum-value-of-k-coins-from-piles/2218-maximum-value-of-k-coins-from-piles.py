class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for c in range(0, k + 1):
                cur = 0
                for coin in range(0, min(len(piles[i - 1]), c) + 1):
                    if coin > 0:
                        cur += piles[i - 1][coin - 1]
                    dp[i][c] = max(dp[i][c],
                                       dp[i - 1][c - coin] + cur)
        return dp[n][k]
        