class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        start = 1
        end = n - 2
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif mid%2 == 0 and nums[mid] == nums[mid-1]:
                end = mid - 1
            elif mid%2 == 1 and nums[mid] == nums[mid+1]:
                end = mid - 1
            else:
                start = mid + 1