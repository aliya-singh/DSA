class Solution(object):
    def reccursion(self, nums, ans, d):
        if len(ans) == len(nums):
            self.l.append(ans[:])
            return
        
        for j in range(len(nums)):
            if j not in d:
                ans.append(nums[j])
                d.append(j)
                self.reccursion(nums, ans, d)
                ans.pop()
                d.pop()


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        ans = []
        d = []
        # for i in range(len(nums)):
        #     d[i] = -1

        self.reccursion(nums, ans, d)
        return self.l