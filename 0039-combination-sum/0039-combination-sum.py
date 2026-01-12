class Solution(object):
    def reccursion(self, candidates, target, i, ans):
        if i == len(candidates):
            if target == 0:
                self.l.append(ans[:])
            return
        
        if candidates[i] <= target:
            ans.append(candidates[i])
            self.reccursion(candidates, target - candidates[i], i, ans)
            ans.pop()
        self.reccursion(candidates, target, i+1, ans)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.l = []
        self.reccursion(candidates, target, 0, [])
        return self.l
