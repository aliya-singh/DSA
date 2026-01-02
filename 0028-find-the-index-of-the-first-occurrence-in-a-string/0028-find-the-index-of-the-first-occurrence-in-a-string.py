class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1

        hc, nc = 0, 0
        while hc < len(haystack):
            if haystack[hc] != needle[nc]:
                hc = hc - nc + 1
                nc = 0
            else:
                if nc == 0:
                    res = hc
                nc += 1
                hc += 1
                if nc == len(needle):
                    break
        
        return res