class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        valid = lambda i,j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        DIR = (0,1,0,-1,0)
        rank = {}
        root = {}
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    root[(i,j)] = (i,j)
                    rank[(i,j)] = 1
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                    rank[rootX] += rank[rootY]
                elif rank[rootX] <= rank[rootY]:
                    root[rootX] = rootY
                    rank[rootY] += rank[rootX]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    for d in range(len(DIR)-1):
                        nr, nc = i + DIR[d], j + DIR[d+1]
                        if valid(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:               
                            union((i,j),(nr,nc))
                            
        return max(rank.values()) if rank.values() else 0