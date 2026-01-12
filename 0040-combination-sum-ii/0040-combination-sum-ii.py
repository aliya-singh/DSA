class Solution(object):
    def reccursion(self, candidates, target, i, ans):
        if i == len(candidates):
            if target == 0:
                self.l.append(ans[:])
            return 
        
        if candidates[i] <= target:
            ans.append(candidates[i])
            self.reccursion(candidates, target - candidates[i], i+1, ans)
            ans.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1 
        self.reccursion(candidates, target, i+1, ans)


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.l = []
        candidates.sort()
        self.reccursion(candidates, target, 0, [])
        return self.l

