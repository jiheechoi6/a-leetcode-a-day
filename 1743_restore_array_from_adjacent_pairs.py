class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs: 
            graph[u].append(v)
            graph[v].append(u)
        
        ans = []
        seen = set()

        stack = []
        for x in graph:
            if len(graph[x]) == 1:
                stack.append(x)
                break
                
        while stack: 
            n = stack.pop()
            ans.append(n)
            seen.add(n)
            for nn in graph[n]: 
                if nn not in seen: stack.append(nn)
        return ans 
