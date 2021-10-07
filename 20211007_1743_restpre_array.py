class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        start_point = set()
        graph = collections.defaultdict(list)
        
        for node1, node2 in adjacentPairs:
            if node1 in start_point:    
                start_point.remove(node1)
            else:
                start_point.add(node1)
            if node2 in start_point:    
                start_point.remove(node2)
            else:
                start_point.add(node2)
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        start = start_point.pop()
        end = start_point.pop()
        
        seen = set()
        seen.add(start)
        queue = [start]
        result = [start]
        for node in queue:
            if node == end:
                return result
            for node in graph[node]:
                if node not in seen:
                    seen.add(node)
                    result.append(node)
                    queue.append(node)
                    
        return result
