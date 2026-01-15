class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        mi = float("inf")
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = n - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                res = abs(sum-target)
                if res < mi:
                    ans = sum
                    mi = res
                if target > sum:
                    start += 1
                elif target < sum:
                    end -= 1
                else:
                    return target
                
            
        return ans
