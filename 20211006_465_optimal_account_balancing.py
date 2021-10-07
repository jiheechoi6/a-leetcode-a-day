class Solution:
    min_trx = math.inf
    def minTransfers(self, transactions: List[List[int]]) -> int:
        graph = collections.defaultdict(int)
        for i1, i2, amount in transactions:
            graph[i1] -= amount
            graph[i2] += amount
            
        graph = [i for i in graph.values() if i !=0]
        return self.backtrack(graph, 0, 0)
        
    def backtrack(self, graph, idx, trx):
        if idx >= len(graph):
            return trx
        if graph[idx] == 0:
            return self.backtrack(graph, idx+1, trx)
        if self.min_trx <= trx:
            return trx

        for i in range(idx+1, len(graph)):
            if graph[idx]*graph[i] < 0:
                graph[i] += graph[idx]
                self.min_trx = self.backtrack(graph, idx+1, trx+1)
                graph[i] -= graph[idx]
                
        return self.min_trx
        
