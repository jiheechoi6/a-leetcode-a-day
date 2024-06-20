class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()
        deck = sorted(deck)

        for d in deck[::-1]:
            q.rotate()
            q.appendleft(d)

        return list(q)
