class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = -float("inf")
        curr = 0
    
        for i in nums:
            curr += i
            sum = max(curr, sum)
            if curr < 0:
                curr = 0
        
        return sum