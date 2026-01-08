class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
