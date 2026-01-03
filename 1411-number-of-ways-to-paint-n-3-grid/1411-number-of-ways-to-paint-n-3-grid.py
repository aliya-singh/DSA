class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        
        aba = 6
        abc = 6

        for _ in range(2, n+1):
            aba, abc = ((aba*3 + abc*2) % mod, (aba*2 + abc*2) % mod)

        return (aba + abc) % mod 