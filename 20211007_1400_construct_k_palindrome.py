class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        cnt = Counter(s)
        oddcount = 0
        for key in cnt:
            if cnt[key]%2 == 1:
                oddcount += 1
            if oddcount>k:
                return False
        return True
