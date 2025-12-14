class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums.sort()
        x = 1
        ans = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            elif (nums[i] + 1) == nums[i+1]:
                x += 1
            else:
                ans = max(ans, x)
                x = 1
        ans = max(ans, x)
        return ans

