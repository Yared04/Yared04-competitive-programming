class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        drxn = [(0,1), (1,0), (1,1), (0,-1), (-1, 0), (1, -1), (-1, 1), (-1,-1)]
        visited = set()
        q = collections.deque([])
        if grid[0][0] == 0:
            q.append((0, 0, 0))
            visited.add((0,0))
        while q:
            cur_r, cur_c, count = q.popleft()
            if cur_r == len(grid)-1 and cur_c == len(grid[0])-1:
                return count + 1
            for r, c in drxn:
                nr, nc = cur_r + r, cur_c + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr, nc ) not in visited:
                    q.append((nr, nc, count + 1))
                    visited.add((nr, nc))
        return -1
            
        
        