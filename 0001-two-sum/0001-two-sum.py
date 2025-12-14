class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n-1):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
