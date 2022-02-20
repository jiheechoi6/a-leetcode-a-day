class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []  # distance, x, y
        for p in points:
            if len(dist) == k:
                heappushpop(dist, (-(p[0]*p[0]+p[1]*p[1]), p[0], p[1]))               
            else:
                heappush(dist, (-(p[0]*p[0]+p[1]*p[1]), p[0], p[1]))
        
        return [(x, y) for (d, x, y) in dist]
