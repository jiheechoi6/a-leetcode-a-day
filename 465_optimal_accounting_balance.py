class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = Counter()
        for fr, to, amt in transactions:
            balance[fr] -= amt
            balance[to] += amt
        
        arr = list(balance.values())

        def backtrack(arr, idx):
            if idx == len(arr):
                return 0
            if arr[idx] == 0:
                return backtrack(arr, idx+1)

            min_tran = math.inf
            for j in range(idx+1, len(arr)):
                if arr[idx] * arr[j]<0:
                    arr[j] += arr[idx]
                    min_tran = min(min_tran, backtrack(arr, idx+1) + 1)
                    arr[j] -= arr[idx]

            return min_tran

        return backtrack(arr, 0)
