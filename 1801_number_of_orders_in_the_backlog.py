class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys, sells = [], []  # (price, count)

        for price, cnt, t in orders:
            if t == 0: heappush(buys, [-price, cnt])
            else: heappush(sells, [price, cnt])

            while buys and sells and -buys[0][0] >= sells[0][0]:
                successCnt = min(buys[0][1], sells[0][1])

                buys[0][1] -= successCnt
                sells[0][1] -= successCnt

                if buys[0][1] == 0: heappop(buys)
                if sells[0][1] == 0: heappop(sells)

        return sum(cnt for _, cnt in buys + sells) % (10**9 + 7)
