class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                pref, suf = word[:i], word[i:]

                if (pref in s and suf in s) or (pref in s and dfs(suf)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False
        
        return [word for word in words if dfs(word)]
        
