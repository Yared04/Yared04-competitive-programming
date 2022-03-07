class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        DIR = (0,1,0,-1,0)
        q = [(grid[0][0],0,0)]
        time = grid[0][0]
        bound =  lambda r,c : 0 <= r and 0 <= c and r < len(grid) and c < len(grid[0])
        while q:
            element, row, col = heapq.heappop(q)
            if time < element:
                time += (element - time)

            if element == grid[-1][-1]:
                return time
            visited.add(element)
            
            for d in range(len(DIR)-1):
                new_row, new_col = row + DIR[d], col + DIR[d+1]
                if bound(new_row, new_col) and grid[new_row][new_col] not in visited:
                    heapq.heappush(q,(grid[new_row][new_col],new_row,new_col))
        
                    
                
            
        