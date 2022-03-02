class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            left = 0
            right = len(grid[i])-1
            first_app = len(grid[i])
            while left <= right:
                
                mid = (left + right)//2
                # print(mid)
                if grid[i][mid] >= 0:
                    left = mid + 1
                elif grid[i][mid] < 0:
                    first_app = mid
                    right = mid-1
            res += len(grid[i]) - first_app
        return res
                    
                    
                