class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        DIR = (0,1,0,-1,0)
        self.res = 0
        inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col  < len(grid[0])
        
        
        def dfs(row, col):
            seen.add((row,col))
            for i in range(len(DIR)-1):
                newRow = row + DIR[i]
                newCol = col + DIR[i+1]
                if not inBound(newRow, newCol) or grid[newRow][newCol] == 0:
                    self.res += 1
                elif (newRow, newCol) not in seen and inBound(newRow, newCol) and grid[newRow][newCol]==1:
                    dfs(newRow, newCol)
        flag = False
        for i in range(len(grid)):
            if flag: break
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    flag = True
                    break
 
        return self.res
        
                    
                
            