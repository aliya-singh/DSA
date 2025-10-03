class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        m = n / 2
        d = {}

        for i in range(n):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        
        for i in d:
            if d[i] > m:
                return i