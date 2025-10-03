class Solution(object):
    def factorial(self, a):
        result = 1
        for i in range(2, a+1):
            result *= i
        return result

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x = m + n - 2
        r = m - 1
        d = x - r
        xf = factorial(x)
        xr = factorial(r)
        xd = factorial(d)

        resultt = xf/(xr*xd)

        return resultt




        