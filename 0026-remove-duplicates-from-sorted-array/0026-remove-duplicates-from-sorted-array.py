class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for i in range(1, len(nums)):
            if nums[idx] != nums[i]:
                idx = idx + 1
                nums[idx] = nums[i]
        
        return idx + 1

