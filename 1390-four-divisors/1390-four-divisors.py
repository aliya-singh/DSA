class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            temp = set()
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    temp.add(j)
                    temp.add(i//j)
                if len(temp) > 4:
                    break
            if len(temp) == 4:
                ans += sum(temp)

        return ans