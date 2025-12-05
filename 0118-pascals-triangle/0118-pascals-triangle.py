class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        l = []
        for i in range(numRows):
            li = []
            for j in range(i+1):
                if j == 0 or j == i:
                    li.append(1)
                else:
                    li.append(l[i-1][j-1] + l[i-1][j])
            
            l.append(li)
        
        return l