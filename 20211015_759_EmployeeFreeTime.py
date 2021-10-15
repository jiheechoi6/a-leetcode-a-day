class Solution:
    cache= None
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        
        self.cache = collections.defaultdict(int)
        return self.schedule(jobs, 0)
            
    def schedule(self, jobs, idx):
        if idx == len(jobs):
            return 0
        if idx in self.cache:
            return self.cache[idx]
        
        _, end, profit = jobs[idx]
        next_i = idx
        while next_i < len(jobs) and jobs[next_i][0]< end:
            next_i +=1 
            
        max_profit = max(self.schedule(jobs, idx+1), profit + self.schedule(jobs, next_i))
        self.cache[idx] = max_profit
        
        return max_profit
