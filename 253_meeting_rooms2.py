h =[]
        # sort = sorted(intervals)
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            # need a new meeting room
            if h == [] or h[0] >i[0]:
                heapq.heappush(h,i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h,i[1])
        return len(h)
