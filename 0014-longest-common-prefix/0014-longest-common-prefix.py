class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        n = len(strs)
        if n == 1:
            return strs[0]
        
        s = ""
        a = ""
        for i in range(len(strs[0])):
            a = strs[0][i]
            for j in range(1, n):
                if i >= len(strs[j]) or strs[j][i] != a:
                    return s
            s += a
        
        return s