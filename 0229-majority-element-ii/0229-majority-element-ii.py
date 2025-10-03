class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = n / 3
        l = []
        nums.sort()
        count = 1
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                if count > m:
                    l.append(nums[i-1])
                count = 1
        if count > m:
            l.append(nums[n-1])
        return l
