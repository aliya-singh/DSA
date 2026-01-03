class Solution(object):
    def reccursion(self, nums, ans, i):
        if i == len(nums):
            self.l.append(ans[:])
            return
        
        ans.append(nums[i])
        self.reccursion(nums, ans, i+1)
        ans.pop()
        i = i+1
        while i < len(nums) and nums[i-1] == nums[i]:
            i = i+1
        
        self.reccursion(nums, ans, i)


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        i = 0
        nums.sort()
        self.reccursion(nums, ans, i)
        return self.l
        