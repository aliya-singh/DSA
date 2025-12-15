class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        d = {}
        max_len = 0
        left = 0

        for i in range(n):
            if s[i] in d and d[s[i]] >= left:
                left = d[s[i]] + 1

            d[s[i]] = i
            max_len = max(max_len, i - left + 1)

        return max_len

            
