class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        neg = -float("inf")
        dp = [[neg] * (m + 1) for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                take = nums1[i] * nums2[j] + max(0, dp[i+1][j+1])
                skip1 = dp[i][j+1]
                skip2 = dp[i+1][j]

                dp[i][j] = max(skip1, skip2, take)
        
        return dp[0][0]