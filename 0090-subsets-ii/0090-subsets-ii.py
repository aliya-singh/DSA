class Solution(object):
    def subset(self, ans, nums, i):
        if i == len(nums):
            if ans[:] not in self.l:
                self.l.append(ans[:])
            return

        ans.append(nums[i])
        self.subset(ans, nums, i+1)
        ans.pop()
        self.subset(ans, nums, i+1)


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        nums.sort()
        self.subset(ans, nums, 0)
        return self.l
        