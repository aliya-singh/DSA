class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = ""
        ans = 0
        for i in s:
            if i not in a:
                a += i
            else:
                a = a[a.index(i)+1:] + i
            
            ans = max(ans, len(a))

        return ans