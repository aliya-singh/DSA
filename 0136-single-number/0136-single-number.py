class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(0, n-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]