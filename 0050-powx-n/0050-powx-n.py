class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        result = 1.0
        m = abs(n)
        while m > 0:
            if m % 2 == 1:
                result *= x
                m = m - 1
            else:
                x = x * x
                m = m / 2

        if n < 0:
            result = 1 / result

        return result

