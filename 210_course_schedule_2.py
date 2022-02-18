from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for p in prerequisites:
            indegree[p[0]] += 1
            outdegree[p[1]].append(p[0])
        ret, start = [], [i for i in range(numCourses) if not indegree[i]]
        while start: # start contains courses without prerequisites
            new = start.pop()
            ret.append(new)
            for j in outdegree[new]:
                indegree[j]-=1
                if not indegree[j]: start.append(j)
                    
        return ret if len(ret) == numCourses else [] # can finish if ret contains all courses 
    
        
                    
              
            
