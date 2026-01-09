class Solution(object):   
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fact(a):
            f = 1
            for i in range(2, a+1):
                f *= i
            
            return f
        
        a = fact(n+m-2)
        b = fact(n-1)
        c = fact(m-1)
        print(a, b, c)
        return a / (b*c)
        