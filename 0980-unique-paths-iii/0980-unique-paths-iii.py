class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.visited = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        inBound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        self.answer = 0
        
        def dfs(row, col):
            if grid[row][col] == 2 and self.visited.bit_count() == m * n:
                self.answer += 1
            
            for r, c in directions:
                nr, nc = row + r, col + c
                if inBound(nr, nc) and not self.visited & 1<<((nr+1)*m+(nc+1)) and grid[nr][nc] != -1:
                    
                    self.visited ^= 1<<((nr+1)*m+(nc+1))
                    dfs(nr, nc)
                    self.visited ^= 1<<((nr+1)*m+(nc+1))     
                    
        starting = (0,0)
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    starting = (i, j)
                    self.visited |= 1<<((i+1)*m+(j+1)) 
                if grid[i][j] == -1:
                    self.visited |= 1<<((i+1)*m+(j+1))

        dfs(starting[0], starting[1])
        return self.answer
                    
                    