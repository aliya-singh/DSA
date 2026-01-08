class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # n = len(grid) * len(grid[0])
        l = []
        for i in grid:
            for j in i:
                l.append(j)

        l.sort()
        rep = mis = -1
        for i in range(1, len(l)):
            if i > 0 and l[i-1] == l [i]:
                rep = l[i]
            if i not in l and mis == -1:
                mis = i
        if mis == -1:
            mis = len(l)
        return [rep, mis]
            

