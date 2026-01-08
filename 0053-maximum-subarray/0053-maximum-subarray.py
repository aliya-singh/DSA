class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -float("inf")
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            max_num = max(sum, max_num)
            sum = max(0, sum)
        
        return max_num
