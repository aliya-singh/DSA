class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        ans = 1
        a = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i]+1 == nums[i+1]:
                a += 1
            else:
                a = 1
            
            ans = max(ans, a) 
        
        return ans
