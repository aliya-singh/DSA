class Solution(object):
    def reccursion(self, nums, ans, i):
        if i == len(nums):
            self.l.append(ans[:])
            return
        
        ans.append(nums[i])
        self.reccursion(nums, ans, i+1)
        ans.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1 
        self.reccursion(nums, ans, i+1)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        nums.sort()
        self.reccursion(nums, [], 0)
        return self.l