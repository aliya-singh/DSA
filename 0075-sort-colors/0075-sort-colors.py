class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        
        nums[0:zero] = [0] * zero
        nums[zero:zero+one] = [1] * one
        nums[zero+one:] = [2] * two