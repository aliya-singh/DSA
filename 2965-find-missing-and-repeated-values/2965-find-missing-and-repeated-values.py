class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        l = []
        for i in grid:
            for j in i:
                l.append(j)
        
        l.sort()
        mis = -1
        if l[0] != 1:
            mis = 1
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                rep = l[i]
            elif l[i] + 1 != l[i+1] and mis == -1:
                mis = l[i] + 1
        if mis == -1:
            mis = len(l)
        return [rep, mis]
            

