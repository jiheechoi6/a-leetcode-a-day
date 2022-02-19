class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        roots = [-1]*(m*n)
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        ans = []
        num = 0
        
        for row, col in positions:
            idx = row*n+col
            
            if roots[idx] != -1:    
                ans.append(num)
                continue
            
            num+=1
            roots[idx] = idx
            for d in dirs:
                new_row, new_col = row+d[0], col+d[1]
                new_idx = new_row*n+new_col
                if new_row<0 or new_row>=m or new_col<0 or new_col>=n or roots[new_idx] == -1:
                    continue
                
                root = self.findRoot(roots, idx)
                new_root = self.findRoot(roots, new_idx)

                if root != new_root:
                    num-=1
                    
                    min_root = min(root, new_root)
                    roots[idx] = min_root
                    roots[new_idx] = min_root
                    roots[root] = min_root
                    roots[new_root] = min_root
                    
            ans.append(num)
        
        return ans
                    
    def findRoot(self, roots, idx):
        if roots[idx] == idx: return idx
        return self.findRoot(roots, roots[idx])
