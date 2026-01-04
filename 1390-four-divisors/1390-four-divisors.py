class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            div = set()
            for i in range(1, int(n**0.5 + 1)):
                if n % i == 0:
                    div.add(i)
                    div.add(n//i)
                
                if len(div) > 4:
                    break
            
            if len(div) == 4:
                ans += sum(div)
        
        return ans