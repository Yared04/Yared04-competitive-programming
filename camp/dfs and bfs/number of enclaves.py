class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # visited = set()
        DIR = (0,1,0,-1,0)
        answer = 0
        def isValid(row,col):
            return (row >= 0) and (col >= 0) and (row < len(grid)) and (col < len(grid[row])) 
            
        def dfs(row, col):
                if grid[row][col] == 1 and (row,col):
                    grid[row][col] = 0
                    # visited.add((row,col))
                    self.count += 1
                    if (row == 0  or col == 0 or row == len(grid)-1 or col == len(grid[row])-1):
                            self.flag = False
                    for j in range(len(DIR)-1):
                        new_row, new_col = row + DIR[j], col + DIR[j+1]
                        if isValid(new_row,new_col) and grid[new_row][new_col] == 1:
                            dfs(new_row,new_col)
                else:
                    return
                                   
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                self.count = 0
                self.flag = True
                dfs(i,j)
                if not self.flag:
                    self.count = 0
                answer += self.count
        return answer
    
                    