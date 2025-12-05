class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        x = -2
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                x = i - 1
                break

        if x == -2:
            nums.reverse()
            return

        for i in range(n-1, x, -1):
            if nums[x] < nums[i]:
                nums[i], nums[x] = nums[x], nums[i]
                break
        
        nums[x+1:] = reversed(nums[x+1:])


