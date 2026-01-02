class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        ds = {}
        dt = {}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] += 1
            
            if t[i] not in dt:
                dt[t[i]] = 1
            else:
                dt[t[i]] += 1
        
        if len(ds) != len (dt):
            return False
        
        for i in ds:
            if i in dt and ds[i] == dt[i]:
                continue
            else:
                return False
        
        return True