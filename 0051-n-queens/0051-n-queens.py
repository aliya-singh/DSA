class Solution(object):
    def isvalid(self, board, row, col, n):        
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i = i-1
            j = j-1
        
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def reccursion(self, board, n, i):
        if i == n:
            solution = []
            for z in range(len(board)):
                s = ""
                for j in range(len(board)):
                    s += board[z][j]
                solution.append(s)
            self.l.append(solution)
            return 
                
        
        for j in range(n):
            if self.isvalid(board, i, j, n):
                board[i][j] = 'Q'
                self.reccursion(board, n, i+1)
                board[i][j] = '.'


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        s = "." * n
        self.l = []
        # board = []
        # for i in range(n):
        #     board.append(s)
        board = [['.' for _ in range(n)] for _ in range(n)]
        print(board)
        self.reccursion(board, n, 0)
        return self.l
        