class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)] 
        box = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i // 3) * 3 + (j // 3)].add(board[i][j])
                else:
                    empty.append((i, j))

        def backtraking(idx):
            if idx == len(empty):
                return True
            
            i, j = empty[idx]
            x = ((i // 3)) * 3 + ((j // 3))
            for dig in "123456789":
                if dig not in row[i] and dig not in col[j] and dig not in box[x]:
                    board[i][j] = dig
                    row[i].add(dig)
                    col[j].add(dig)
                    box[x].add(dig)

                    if backtraking(idx + 1):
                        return True
                    
                    board[i][j] = "."
                    row[i].remove(dig)
                    col[j].remove(dig)
                    box[x].remove(dig)
            
            return False
        
        backtraking(0)






