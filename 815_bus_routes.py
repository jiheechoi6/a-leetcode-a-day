class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        
        stopBoard = {} 
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)
        
        queue = deque([S])
        visited = set()

        res = 0
        while queue:
            res += 1

            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                for bus in stopBoard[curStop]:
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T: return res
                        queue.append(stop)
        return -1
