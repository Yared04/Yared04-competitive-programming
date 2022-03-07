class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = collections.deque()
        time = 0
        Dir = (0,1,0,-1,0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                
                    
        while q:
            (x, y, time) = q.popleft()
            visited.add((x,y))
            for i in range(len(Dir)-1):
                cx, cy = x + Dir[i], y + Dir[i+1]
                if (cx, cy) not in visited and (cx >= 0 and cy >= 0 and cx < len(grid) and cy < len(grid[0])):
                    if grid[cx][cy] == 0:
                        visited.add((cx, cy))
                    elif grid[cx][cy] == 1:
                        grid[cx][cy] = 2
                        q.append((cx,cy, time+1))
                        visited.add((cx,cy))
                    elif grid[cx][cy] == 2:
                        visited.add((cx,cy))
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                if (i,j) not in visited and grid[i][j] == 1:
                    return -1
                
        return time
                        
                        
                        
            
            
        