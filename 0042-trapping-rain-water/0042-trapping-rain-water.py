class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l1 = [height[0]]

        for i in range(1, n):
            if l1[i-1] > height[i]:
                l1.append(l1[i-1])
            else:
                l1.append(height[i])

        l2 = [0] * n
        l2[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            if l2[i+1] < height[i]:
                l2[i] = height[i]
            else:
                l2[i] = l2[i+1]
        
        count = 0
        for i in range(n):
            count += min(l1[i], l2[i]) - height[i]
        
        return count




