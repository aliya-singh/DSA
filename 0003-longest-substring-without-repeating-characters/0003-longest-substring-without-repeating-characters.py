class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        a = ""
        m = 0
        for i in range(n):
            if s[i] not in a:
                a += s[i]
            else:
                a = a[a.index(s[i]) + 1:] + s[i]
        
            m = max(m, len(a))
        

        return m




        