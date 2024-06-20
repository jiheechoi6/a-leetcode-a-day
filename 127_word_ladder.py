class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = collections.deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for a in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + a + word[i+1:]
                    if new_word in words:
                        q.append((new_word, length + 1))
                        words.remove(new_word)
        
        return 0
