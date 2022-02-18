class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            adjList[c1].append(c2)

        state = [0] * numCourses

        def hasCycle(v):
            if state[v] == 1:
                return False
            if state[v] == -1:
                return True

            state[v] = -1

            for i in adjList[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True
