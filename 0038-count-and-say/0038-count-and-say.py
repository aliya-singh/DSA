class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        if n == 1:
            return s
        
        for _ in range(n-1):
            i = 0
            ans = ""
            while i < len(s):
                c = 1
                a = s[i]
                if i < len(s) - 1 and a != s[i+1]:
                    ans += str(c)
                    ans += str(s[i])
                    i += 1
                elif i < len(s) - 1 and a == s[i+1]:
                    while i < len(s) - 1 and a == s[i+1]:
                        c += 1
                        i += 1
                    i += 1
                    ans += str(c)
                    ans += str(a)
                else:
                    ans += str(c)
                    ans += str(s[i])
                    i += 1
            s = ans
        
        return s






                

                


