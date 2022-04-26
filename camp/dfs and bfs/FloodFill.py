class Solution:
    def dfs(self, image, row, col, oldColor, newColor,visited):
            visited.add((row,col))
            for d in range(len(self.DIR)-1):
                new_row, new_col = row + self.DIR[d], col + self.DIR[d+1]
                if not self.in_bound(new_row, new_col) or image[new_row][new_col] != oldColor or (new_row,new_col) in visited:
                    continue
                self.dfs(image, new_row, new_col, oldColor, newColor,visited)
            image[row][col] = newColor
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            visited = set()
            self.DIR = (1, 0, -1, 0, 1)
            self.in_bound = lambda row, col: 0 <= row < len(image) and 0 <= col < len(image[0])
            oldColor = image[sr][sc]
            self.dfs(image, sr, sc, oldColor, newColor,visited)
            return image
