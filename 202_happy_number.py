class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        cur = n
        while True:
            if cur in visited: return False
            visited.add(cur)
            
            newcur = 0
            for digit in str(cur): newcur += int(digit)**2
            if newcur == 1: return True
            cur = newcur
