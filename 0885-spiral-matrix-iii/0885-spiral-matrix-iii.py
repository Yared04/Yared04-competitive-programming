class Solution:
    def inBound(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coordinates = []
        horizontal_move = 1
        vertical_move = 1
        cur_row = rStart
        cur_col = cStart
        direction = 1
        
        while len(coordinates) < rows * cols:
            for i in range(1, horizontal_move + 1):
                if self.inBound(cur_row, cur_col, rows, cols):
                    coordinates.append([cur_row, cur_col])
                cur_col += direction * 1

            for i in range(1, vertical_move + 1):
                if self.inBound(cur_row, cur_col, rows, cols):
                    coordinates.append([cur_row, cur_col])
                cur_row += direction * 1
            
            direction *= -1
            horizontal_move += 1
            vertical_move += 1
        return coordinates
                