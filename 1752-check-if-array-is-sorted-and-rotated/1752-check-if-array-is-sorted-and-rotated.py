class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                c += 1
                if c > 1:
                    return False
        
        if c == 1:
            if nums[-1] <= nums[0]:
                return True
            else:
                return False
        
        return True
    