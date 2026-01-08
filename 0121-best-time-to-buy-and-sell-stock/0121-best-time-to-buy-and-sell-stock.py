class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if m > prices[i]:
                m = prices[i]
            else:
                profit = max(profit, (prices[i] - m))
        
        return profit