class Solution(object):
    def reccursion(self, candidates, target, ans, i):
        if i == len(candidates):    
            if target == 0:
                self.l.append(ans[:])
            return
        
        if candidates[i] <= target:
            ans.append(candidates[i])
            self.reccursion(candidates, target - candidates[i], ans, i+1)
            ans.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1
        self.reccursion(candidates, target, ans, i+1)

        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        candidates.sort()
        self.reccursion(candidates, target, ans, 0)
        return self.l