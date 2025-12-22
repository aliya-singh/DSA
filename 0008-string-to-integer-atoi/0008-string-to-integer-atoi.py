class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        ans = 0
        neg = False
        for i in range(len(s)):
            if i == 0 and s[i] == "-":
                neg = True
            elif i == 0 and s[i] == "+":
                continue
            elif s[i].isdigit():
                ans = int(s[i]) + ans*10
            else:
                break
        if neg:
            ans *= -1
        
        min_int = -2**31
        max_int = 2**31 - 1
        
        if min_int > ans:
            return min_int
        if max_int < ans:
            return max_int
        return ans
            
              
            
            