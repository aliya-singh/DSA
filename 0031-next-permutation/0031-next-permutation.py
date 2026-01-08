class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        temp = -2
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                temp = i-1
                break
        
        if temp == -2:
            nums.reverse()
            return
        
        for i in range(n-1, temp, -1):
            if nums[temp] < nums[i]:
                nums[temp], nums[i] = nums[i], nums[temp]
                break
        
        nums[temp+1:] = reversed(nums[temp+1:])
        