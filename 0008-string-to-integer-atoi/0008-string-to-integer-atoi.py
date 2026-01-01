class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        sign = False
        res = 0
        for i in range(len(s)):
            if i == 0 and s[i] == "-":
                sign = True
            elif i == 0 and s[i] == "+":
                continue
            elif s[i].isdigit():
                res = int(s[i]) + res * 10
            else:
                break
        
        if sign:
            res = res * (-1)
        
        mp = 2**31 - 1
        mn = - 2**31

        if sign:
            if res < mn:
                return mn
            else:
                return res 

        if res > mp:
            return mp
        else:
            return res

            
              
            
            