class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd = n/2
        even = n/2 + n%2
        ans = 5**even * 4**odd
        return ans % (10**9 + 7)