class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        cn, cm = 0, 0
        ans = 0
        while cn < n and cm < m:
            if g[cn] <= s[cm]:
                ans += 1
                cn += 1
            cm += 1
        return ans
