class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(arr):
            elements = set()
            for entry in arr:
                if entry in elements: return False
                if entry != ".":
                    elements.add(entry)
            return True
                    
        
        def checkCol(idx):
            elements = set()
            for entry in board:
                if entry[idx] in elements: return False
                if entry[idx] != ".":
                    elements.add(entry[idx])
            return True
            
            
        def checkSubBox(startRow, endRow, startCol, endCol):
            elements = set()
            for i in range(startRow, endRow):
                for j in range(startCol, endCol):
                    if board[i][j] in elements: return False
                    if board[i][j] != ".":
                        elements.add(board[i][j])
            return True
        
        for i in range(len(board)):
            row = checkRow(board[i])
            col = checkCol(i)
            if not row or not col:
                break
      
        subBox = checkSubBox(0,3,0,3) and checkSubBox(0,3,3,6) and checkSubBox(0,3,6,9) and checkSubBox(3,6,0,3) and checkSubBox(3,6,3,6) and checkSubBox(3,6,6,9) and checkSubBox(6,9,0,3) and checkSubBox(6,9,3,6) and checkSubBox(6,9,6,9)
        return row and col and subBox
        
            
                
            
        