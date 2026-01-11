class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = float("inf")
        for i in range(n-1):
            start = i + 1
            end = n - 1
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if abs(target - ans) > abs(target - sum):
                    ans = sum
                if target > sum:
                    start += 1
                elif target < sum:
                    end -= 1
                else:
                    return target
        
        return ans