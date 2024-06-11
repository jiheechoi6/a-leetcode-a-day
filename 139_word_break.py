class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def construct(cur):
            if not cur:
                return True
            if cur in memo:
                return memo[cur]

            for word in wordDict:
                if cur.startswith(word):
                    if construct(cur[len(word):]):
                        memo[cur] = True
                        return True
            
            memo[cur] = False
            return False
        
        return construct(s)
