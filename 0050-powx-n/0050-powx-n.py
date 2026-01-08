class Solution(object):        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        pow = 1
        neg = False
        if n < 0:
            neg = True
        n = abs(n) 
        while n > 0:
            if n % 2 == 1:
                pow *= x
                n = n-1
            else:
                x = x*x
                n = n//2
        
        if neg:
            return 1/pow
        return pow
