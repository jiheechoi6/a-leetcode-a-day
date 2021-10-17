class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts = sorted(starts)
        ends = sorted(ends)
        
        latest_end_i = 0
        roomnum = 1
        
        for start_idx in range(1, len(starts)):
            if starts[start_idx] < ends[latest_end_i]:  # need new room
                roomnum += 1
            else:
                latest_end_i += 1
                
        return roomnum
        
