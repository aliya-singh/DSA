class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        sum = 0
        ncount = 0
        min = float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                sum += abs(matrix[i][j])
                if min > abs(matrix[i][j]):
                    min = abs(matrix[i][j])
                
                if matrix[i][j] < 0:
                    ncount += 1
        
        if ncount%2 == 0:
            return sum
        else:
            return sum - 2*min
        
