class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        c = 0

        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                c += 1
                if c > 1:
                    return False
        
        if nums[n-1] > nums[0] and c == 1:
            return False
        else:
            return True