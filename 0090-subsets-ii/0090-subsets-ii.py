class Solution(object):
    def subset(self, nums, ans, i):
        if i == len(nums):
            if ans[:] not in self.l:
                self.l.append(ans[:])
            return
        
        ans.append(nums[i])
        self.subset(nums, ans, i+1)
        ans.pop()
        self.subset(nums, ans, i+1)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        nums.sort()
        self.subset(nums, ans, 0)
        return self.l

        