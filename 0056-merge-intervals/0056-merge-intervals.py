class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        l = []
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_start <= end:
                end = max(curr_end, end)
            else:
                l.append([start, end])
                start = curr_start
                end = curr_end
        l.append([start, end])
        return l
