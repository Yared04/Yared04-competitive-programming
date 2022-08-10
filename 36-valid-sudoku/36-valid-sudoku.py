class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(arr):
            count = 0
            elements = set()
            for entry in arr:
                if entry != ".":
                    count += 1
                    elements.add(entry)
            return count == len(elements)
                    
        
        def checkCol(idx):
            count = 0
            elements = set()
            for entry in board:
                if entry[idx] != ".":
                    count += 1
                    elements.add(entry[idx])
            return count == len(elements)
            
            
        def checkSubBox(startRow, endRow, startCol, endCol):
            count = 0
            elements = set()
            for i in range(startRow, endRow):
                for j in range(startCol, endCol):
                    if board[i][j] != ".":
                        count += 1
                        elements.add(board[i][j])
            return count == len(elements)
        
        for i in range(len(board)):
            row = checkRow(board[i])
            if not row:
                break
        for i in range(len(board)):
            col = checkCol(i)
            if not col:
                break
        subBox = checkSubBox(0,3,0,3) and checkSubBox(0,3,3,6) and checkSubBox(0,3,6,9) and checkSubBox(3,6,0,3) and checkSubBox(3,6,3,6) and checkSubBox(3,6,6,9) and checkSubBox(6,9,0,3) and checkSubBox(6,9,3,6) and checkSubBox(6,9,6,9)
        return row and col and subBox
        
            
                
            
        