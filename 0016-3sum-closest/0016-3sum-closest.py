class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        curr_sum = float('inf')

        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if abs(target - sum) < abs(target - curr_sum):
                    curr_sum = sum
                
                if target > sum:
                    left += 1
                elif target < sum:
                    right -= 1
                else: 
                    return target

        return curr_sum
                    



            

