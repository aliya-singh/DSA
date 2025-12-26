class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        a = [0] * n
        b = [0] * m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    a[i] = 1
                    b[j] = 1
        
        for i in range(n):
            for j in range(m):
                if a[i] == 1 or b[j] == 1:
                    matrix[i][j] = 0

