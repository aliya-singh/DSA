class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 1
        curr_count = 0

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
                if count > curr_count:
                    curr_count = count
            else:
                if count > curr_count:
                    curr_count = count

                count = 1
        if count > curr_count and n >= 1:
            return count
        else:
            return curr_count                
