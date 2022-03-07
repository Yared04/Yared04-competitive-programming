class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        to_change = []
        self.DIR = (0,1,0,-1,0)
        visited = set()
        def isValid(r,c):
            return (r >= 0) and (c >= 0) and (r < len(board)) and (c < len(board[r])) and (r,c) not in visited
        def check(row,col):       
            if isValid(row,col) and board[row][col] == "O":
                visited.add((row,col))
                self.changed.append((row,col))
                if (row == 0  or col == 0 or row == len(board)-1 or col == len(board[row])-1):
                    
                        self.flag = False
                for d in range(len(self.DIR)-1):
                    new_row, new_col = row + self.DIR[d], col + self.DIR[d+1]
                    if isValid(new_row,new_col) and board[new_row][new_col] == "O":
                        check(new_row, new_col) 
            else:
                return

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.changed = []
                self.flag = True
                if (i,j) in visited or board[i][j] == "X":
                    continue
                check(i,j)
                if not self.flag:
                    self.changed = []
                to_change.extend(self.changed)
        
        for position in to_change:
            board[position[0]][position[1]] = "X"
    
                    
                