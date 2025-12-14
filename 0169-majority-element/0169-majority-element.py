class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        
        n = len(nums)
        m = n/2
        for i in d.keys():
            if d[i] > m:
                return i
