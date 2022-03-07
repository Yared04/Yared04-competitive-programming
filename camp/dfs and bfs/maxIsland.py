class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIR = (0,1,0,-1,0)
        ans = 0
        
        valid = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        # def valid(r,c):
        #     return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]) 
        def dfs(row,col):
            if valid(row,col) and grid[row][col] == 1:
                self.count += 1
                grid[row][col] = 0
                for d in range(len(DIR)-1):
                    new_row, new_col = row + DIR[d], col + DIR[d+1]
                    if valid(new_row,new_col) and grid[new_row][new_col] == 1:
                        dfs(new_row,new_col)
            
            # print(self.count)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.count = 0
                if grid[i][j] == 0:
                    continue
                dfs(i,j)
                ans = max(ans,self.count)
        return ans
        
        
                
        
        