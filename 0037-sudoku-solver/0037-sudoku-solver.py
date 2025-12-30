class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isvalid(row, col, dig):
            for i in range(9):
                if board[i][col] == dig or board[row][i] == dig:
                    return False
            
            rs = (row//3) * 3
            cs = (col//3) * 3
            for i in range(rs, rs+3):
                for j in range(cs, cs+3):
                    if board[i][j] == dig:
                        return False
            
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in "123456789":
                            if isvalid(i, j, ch):
                                board[i][j] = ch
                                if backtrack():
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        backtrack()