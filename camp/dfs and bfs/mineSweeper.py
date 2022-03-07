class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = set()
        bound = lambda r,c : 0 <= r and 0 <= c and r < len(board) and c < len(board[0])
        def adjacentCheck(x,y):
            mines = 0
            for direc in directions:
                row, col = x + direc[0], y + direc[1]
                if bound(row,col) and board[row][col] == "M":
                    mines += 1
            return mines
        def dfs(row,col):
            visited.add((row,col))
            if board[row][col] == 'E':
                if not adjacentCheck(row,col):
                    board[row][col] = "B"
                    for d in directions:
                        nr, nc = row + d[0] , col + d[1]
                        if bound(nr,nc) and (nr,nc) not in visited:
                            dfs(nr,nc)
                else:
                    board[row][col] = str(adjacentCheck(row,col))
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        dfs(click[0],click[1])
        return board
                    