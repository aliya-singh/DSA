class Solution(object):
    def isvalid(self, board, row, col, n):
        for i in range(row):
            if board[i][col] == "Q":
                return False
        
        for i in range(col):
            if board[row][i] == "Q":
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        
        return True

    def reccursion(self, board, n, row):
        if row == n:
            sol = []
            for i in range(len(board)):
                s = ""
                for j in range(len(board)):
                    s += board[i][j]
                sol.append(s)
            self.l.append(sol)
        
        for col in range(n):
            if self.isvalid(board, row, col, n):
                board[row][col] = "Q"
                self.reccursion(board, n, row + 1)
                board[row][col] = "."

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.l = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.reccursion(board, n, 0)
        return self.l