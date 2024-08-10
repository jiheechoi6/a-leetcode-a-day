class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        conMap = [[] for _ in range(n)]
        # reformat connection map
        for emp in range(len(manager)):
            if manager[emp] != -1: conMap[manager[emp]].append(emp)

        que = deque([(headID, 0)])
        res = 0

        while que:
            informerCnt = len(que)

            for _ in range(informerCnt):
                informer, curTime = que.popleft()
                res = max(res, curTime)
                informerTime = curTime + informTime[informer] # time after informer informs everyone

                for informee in conMap[informer]:
                    que.append((informee, informerTime))

        return res
