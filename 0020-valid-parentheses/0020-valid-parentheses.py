class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                l.append(i)
            
            else:
                if not l:
                    return False
                
                last = l.pop()
                if i == ")" and last != "(":
                    return False
                if i == "}" and last != "{":
                    return False
                if i == "]" and last != "[":
                    return False
        
        if l:
            return False
        return True
                