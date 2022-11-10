class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = {}
        def topDown(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if (i,j) not in memo:
                if word1[i] == word2[j]:
                    memo[(i, j)] = topDown(i+1, j+1)
                else:
                    memo[(i, j)] = 1 + min(topDown(i+1, j), topDown(i, j+1))
            return memo[(i, j)]
        return topDown(0,0)
    
        # n = len(word1)+1
        # dp = [[0] * n for _ in range(len(word2)+1)]
        # for i in range(len(word2)+1):
        #     for j in range(len(word1)+1):
        #         if i == 0 or j == 0:
        #             dp[i][j] = i+j
        #         elif word2[i-1] == word1[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]