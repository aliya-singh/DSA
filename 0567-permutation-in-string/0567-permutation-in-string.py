class Solution(object):
    def hashMap(self, s):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        return d 


    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        ds1 = self.hashMap(s1)
        for i in range(len(s2) - len(s1)):
            s = s2[i: i+len(s1)]
            ds = self.hashMap(s)
            if ds == ds1:
                return True
        
        return False



