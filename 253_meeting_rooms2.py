class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda item: item[0])
        ends = [0]

        for start, end in intervals:
            if start < ends[0]: 
                heappush(ends, end)
            else:
                heapreplace(ends, end)
        
        return len(ends)
