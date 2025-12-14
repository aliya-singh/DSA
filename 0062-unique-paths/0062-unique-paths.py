class Solution(object):
    def factorial(self, m):
        fact = 1
        for i in range(2, m):
            fact *= i
        
        return fact

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        a = factorial(m + n - 2)
        b = factorial(n - 1)
        c = factorial(m - 1)

        return a / (b * c)
        