class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == 0:
                    l.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        
        return l
