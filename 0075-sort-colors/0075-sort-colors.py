class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        z = 0
        o = 0
        t = 0

        for i in nums:
            if i == 0:
                z += 1
            elif i == 1:
                o += 1
            else:
                t += 1
        
        for i in range(z):
            nums[i] = 0
        for i in range(o):
            nums[z+i] = 1
        for i in range(t):
            nums[z+i+o] = 2