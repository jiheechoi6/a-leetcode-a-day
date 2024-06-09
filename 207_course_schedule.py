class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjLst = [[] for _ in range(numCourses)]
        # create adjacency list
        for course, req in prerequisites:
            adjLst[req].append(course)

        inDeg = [0]*numCourses
        for course, _ in prerequisites:
            inDeg[course] += 1
        
        que = []
        for i in range(numCourses):
            if inDeg[i] == 0: # no prerequisites for this course
                que.append(i)
        
        takenCnt = 0
        while que:
            takenCnt += 1
            crs = que.pop(0)

            for nextCrs in adjLst[crs]:
                inDeg[nextCrs] -= 1

                if inDeg[nextCrs] == 0:
                    que.append(nextCrs)
        
        return takenCnt == numCourses
