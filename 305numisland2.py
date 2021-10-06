class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        roots = [-1]*(m*n)
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_num = 0
        for pos in positions:
            r = pos[0]
            c = pos[1]
            idx = r*n + c
            if roots[idx] != -1:  # already visited before
                result.append(island_num)
                continue
            
            roots[idx] = idx
            island_num += 1
            
            for dirc in directions:
                new_r = r + dirc[0]
                new_c = c + dirc[1]
                new_idx = new_r*n + new_c
                
                if new_r<0 or new_r>=m or new_c<0 or new_c>=n or roots[new_idx]==-1:
                    continue
                
                root = self.findRoot(roots, idx)
                new_root = self.findRoot(roots, new_idx)
                
                if root != new_root:
                    island_num -=1
                    
                if root < new_root:
                    roots[new_root] = root
                else:
                    roots[root] = new_root
                    
            result.append(island_num)
                    
        return result
                    
                
    def findRoot(self, roots, idx):
        if roots[idx] == idx:
            return idx
        return self.findRoot(roots, roots[idx])
