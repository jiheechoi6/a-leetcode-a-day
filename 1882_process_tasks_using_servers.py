class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        avail = [(weight, i) for i, weight in enumerate(servers)]  # key -> weight, i
        heapify(avail)
        notavail = [] # key -> end time, weight, i
        
        ans = []
        for time, tlen in enumerate(tasks):
            while (notavail and time >= notavail[0][0]):
                endtime, weight, idx = heappop(notavail)
                heappush(avail, (weight, idx))

            if not avail:
                endtime, weight, idx = heappop(notavail)
                ans.append(idx)
                heappush(notavail, (endtime + tlen, weight, idx))
            else:
                weight, idx = heappop(avail)
                ans.append(idx)
                heappush(notavail, (time + tlen, weight, idx))

        return ans
