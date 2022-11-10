class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp = {}
#         def topDown(i, j):
#             if i == m and j == n:
#                 return 0
#             if i == m:
#                 return n - j
#             if j == n:
#                 return m - i
            
#             if (i, j) not in dp:
#                 if word1[i] == word2[j]:
#                     dp[(i, j)] = topDown(i+1, j+1)
#                 else:
#                     insert = 1 + topDown(i, j+1)
#                     delete = 1 + topDown(i+1, j)
#                     replace = 1 + topDown(i+1, j+1)
#                     dp[(i, j)] = min(insert, delete, replace)
#             return dp[(i,j)]
#         return topDown(0, 0)
        dp = [[-1 for l in range(n+1)] for _ in range(m+1)]
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i-1][j]
                    delete = dp[i][j-1]
                    replace = dp[i-1][j-1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[-1][-1]
                