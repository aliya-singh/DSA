class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        flag = 0
        temp = nums[0]
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                flag += 1
                if flag > 1:
                    return False

        if flag == 1 and nums[0] < nums[-1]:
            return False

        return True