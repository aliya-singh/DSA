class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        count = 0
        piles = sorted([a, b, c])

        while piles[1] > 0:
            piles[1] -= 1
            piles[2] -= 1
            count += 1

            piles.sort()

        return count