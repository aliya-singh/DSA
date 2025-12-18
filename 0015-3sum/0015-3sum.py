class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        l = []
        for i in range(n-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            start = i + 1
            end = n - 1
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if sum == 0:
                    l.append([nums[start], nums[end], nums[i]])
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
                
