class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        if len(routes) == 0:
            return -1
        
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if r1.intersection(r2):
                    graph[i].add(j)
                    graph[j].add(i)
                    
        seen, targets = set(), set()
        queue = []
        for node, route in enumerate(routes):
            if source in route: 
                seen.add(node)
                queue.append((node, 1))
            if target in route: targets.add(node)
        
        # queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
                    
        return -1
        
