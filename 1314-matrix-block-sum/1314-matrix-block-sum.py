class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def calculateSum(rowStart, rowEnd, colStart, colEnd):
            total = 0
            for i in range(rowStart, rowEnd + 1):
                for j in range(colStart, colEnd + 1):
                    total += mat[i][j]
            return total
        
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rowStart = max(0, i - k)
                rowEnd = min(i + k, len(mat) - 1)
                colStart = max(0, j - k)
                colEnd =  min(j + k, len(mat[0]) - 1)
                ans[i][j] = calculateSum(rowStart, rowEnd, colStart, colEnd)
        return ans
                