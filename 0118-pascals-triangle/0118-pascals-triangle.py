class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        l = []
        for i in range(numRows):
            ll = []
            for j in range(i+1):
                if j == 0 or j == i:
                    ll.append(1)
                else:
                    ll.append(l[i-1][j] + l[i-1][j-1])
            
            l.append(ll)

        return l