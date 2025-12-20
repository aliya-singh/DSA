class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = []
        third = -float("inf")
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] < third:
                return True
            
            while l and nums[i] > l[-1]:
                third = l.pop()

            l.append(nums[i])

        return False 

