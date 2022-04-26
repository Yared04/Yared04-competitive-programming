class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def path(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row >= len(triangle) or col >= len(triangle[row]):
                return 0
            s_idx = path(row+1,col)
            n_idx = path(row+1, col+1)
            memo[(row,col)] = triangle[row][col] + min(s_idx,n_idx)
            return memo[(row,col)]
        return path(0,0)