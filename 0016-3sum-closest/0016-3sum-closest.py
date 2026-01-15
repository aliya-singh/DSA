class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        m = float("inf")
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s == target:
                    return target
                if abs(target - s) < m:
                    m = abs(target - s)
                    ans = s
                if s > target:
                    end = end - 1
                else:
                    start = start + 1
        
        return ans