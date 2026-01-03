class Solution(object):
    def reccursion(self, nums, ans, i):
        if i == len(nums):
            self.l.append(ans[:])
            return
        
        ans.append(nums[i])
        self.reccursion(nums, ans, i+1)
        ans.pop()
        self.reccursion(nums, ans, i+1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        self.reccursion(nums, [], 0)
        return self.l


