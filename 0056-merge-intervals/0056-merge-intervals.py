class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        n = len(intervals)
        l = []
        
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        
        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]
            if curr_end >= start:
                curr_end = max(end, curr_end)
            else:
                l.append([curr_start, curr_end])
                curr_start = start
                curr_end = end
        l.append([curr_start, curr_end])
        return l
            