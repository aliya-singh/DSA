class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in digits:
            res = res * 10 + i
        
        res += 1
        digit = []
        while res:
            digit.insert(0, (res % 10))
            res = res // 10
        
        return digit
        