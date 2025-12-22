class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, sol = [], []
        def backtracking(index):
            res.append(sol[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue

                sol.append(nums[i])
                backtracking(i+1)
                sol.pop()

        backtracking(0)
        return res

        