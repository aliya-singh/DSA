class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min = -float("inf")
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            min = max(sum, min)
            if sum < 0:
                sum = 0
        
        return min
