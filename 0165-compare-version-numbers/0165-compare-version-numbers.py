class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = 0, 0
        n, m = len(version1), len(version2)
        while v1 < n and v2 < m:
            s1 = ""
            while v1 < n and version1[v1] != ".":
                s1 += version1[v1]
                v1 += 1
            v1 += 1

            s2 = ""
            while v2 < m and version2[v2] != ".":
                s2 += version2[v2]
                v2 += 1
            v2 += 1

            if int(s1) > int(s2):
                return 1
            elif int(s1) < int(s2):
                return -1
        
        while v1 < n:
            if version1[v1] != "." and int(version1[v1]) > 0:
                return 1
            v1 += 1
        
        while v2 < m:
            if version2[v2] != "." and int(version2[v2]) > 0:
                return -1
            v2 += 1

        return 0