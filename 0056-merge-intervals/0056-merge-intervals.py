class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        n = len(intervals)
        l = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, n):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if curr_start <= end:
                end = max(end, curr_end)
            else:
                l.append([start, end])
                start = curr_start
                end = curr_end
        l.append([start, end])

        return l