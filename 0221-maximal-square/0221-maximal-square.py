class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows + 1)]
        
        max_square = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_square = max(max_square, dp[i+1][j+1])

        return max_square * max_square