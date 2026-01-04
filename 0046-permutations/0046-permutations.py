class Solution(object):
    def reccursion(self, nums, ans, d):
        if len(ans) == len(nums):
            self.l.append(ans[:])
            return

        for i in range(len(nums)):
            if i not in d:
                ans.append(nums[i])
                d.append(i)
                self.reccursion(nums, ans, d)
                d.pop()
                ans.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        d = []
        self.reccursion(nums, ans, d)
        return self.l