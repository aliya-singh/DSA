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
        ans = []
        i = 0
        self.reccursion(nums, ans, i)
        return self.l