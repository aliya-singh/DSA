class Solution(object):
    def reccursion(self, s, ans, i):
        if i == len(s):
            self.l.append(ans[:])
            return 
        
        for j in range(i+1, len(s)+1):
            st = s[i:j]
            if st == st[::-1]:
                ans.append(st)
                self.reccursion(s, ans, j)
                ans.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.l = []
        ans = []
        self.reccursion(s, ans, 0)
        return self.l