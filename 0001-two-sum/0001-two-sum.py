class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        n = len(nums)
        for i in range(n):
            d[nums[i]] = i
        for i in range(n):
            rem = target - nums[i]
            if rem in d and d[rem] != i:
                return [d[rem], i]

        