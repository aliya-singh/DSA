class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) / 3
        d = {} 
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        l = []
        for key, value in d.items():
            if d[key] > n:
                l.append(key)
        
        return l
