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
        ans = []
        for i in range(1, len(l)):
            if l[i-1] == l[i]:
                ans.append(l[i-1])
                break
        
        for i in range(1, len(l)+1):
            if i not in l:
                ans.append(i)
                break

        return ans
            

