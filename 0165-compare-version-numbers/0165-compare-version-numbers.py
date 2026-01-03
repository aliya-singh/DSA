class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = 0, 0
        n1, n2 = len(version1), len(version2)
        while v1 < n1 or v2 < n2:
            res1, res2 = 0, 0
            while v1 < n1 and version1[v1] != ".":
                res1 = res1 * 10 + int(version1[v1])
                v1 += 1
            v1 += 1
            
            while v2 < n2 and version2[v2] != ".":
                res2 = res2 * 10 + int(version2[v2])
                v2 += 1
            v2 += 1

            if res1 < res2:
                return -1
            elif res1 > res2:
                return 1
        
        return 0