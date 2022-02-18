class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])
        ends = [intervals[0][1]]
        ans = 1
        for start, end in intervals[1:]:
            if start < ends[0]:  # new room
                ans+=1
                heapq.heappush(ends, end)
            else:
                heapq.heapreplace(ends, end)
        return ans
