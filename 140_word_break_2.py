class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        res = []
        
        def construct(s, cur):
            if not s: res.append(cur.copy())

            for word in words:
                if s.startswith(word):
                    cur.append(word)
                    construct(s[len(word):], cur)
                    cur.pop()

        construct(s, [])

        return [' '.join(lst) for lst in res]
