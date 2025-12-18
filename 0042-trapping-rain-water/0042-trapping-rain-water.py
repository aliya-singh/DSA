class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        prefix = [height[0]]
        n = len(height)
        for i in range(1, n):
            x = max(prefix[i-1], height[i])
            prefix.append(x)
        
        suffix = [0] * n
        suffix[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            x = max(height[i], suffix[i+1])
            suffix[i] = x
        
        count = 0
        for i in range(n):
            if height[i] < suffix[i] and height[i] < prefix[i]:
                count += min(suffix[i], prefix[i]) - height[i]
        
        return count

