class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set([(0, 0)])
        que = deque([(0, 0)])

        if target > (x + y): return False

        while que:
            state = que.popleft()

            if (state[0] + state[1]) == target: return True

            options = set()

            options.add((state[0], 0))
            options.add((0, state[1]))
            options.add((x, state[1]))
            options.add((state[0], y))
            options.add((state[0] + min(state[1], x - state[0]), state[1] - min(state[1], x - state[0])))
            options.add((state[0] - min(state[0], y - state[1]), state[1] + min(state[0], y - state[1])))

            for option in options:
                if option not in visited:
                    que.append(option)
                    visited.add(option)
        
        return False
