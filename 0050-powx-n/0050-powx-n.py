class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        ans = 1
        m = abs(n)
        while m:
            if m%2 == 1:
                ans *= x
                m = m-1
            else:
                x = x*x
                m = m/2
        
        if n < 0:
            ans = 1/ans
        return ans
