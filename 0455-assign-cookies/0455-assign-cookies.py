class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        count = 0
        n = len(g)
        m = len(s)
        counts = 0
        countg = 0
        while counts < m and countg < n:
            if g[countg] <= s[counts]:
                count += 1
                counts += 1
                countg += 1
            else:
                counts += 1


        return count