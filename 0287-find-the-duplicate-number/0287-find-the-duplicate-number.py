class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return nums[i]