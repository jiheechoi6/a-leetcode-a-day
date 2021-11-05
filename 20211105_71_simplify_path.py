class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        
        for elem in path.split('/'):
            if elem == '..':
                if stk: stk.pop()
            elif elem and elem != '.':
                stk.append(elem)
                
        return '/'+'/'.join(stk)
