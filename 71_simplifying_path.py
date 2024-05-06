class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path_list = path.split('/')

        for elem in path_list:
            if elem == '..' and len(stk):
                stk.pop()
            elif elem != '' and elem != '.' and elem != '..':
                stk.append(elem)

        return '/'+'/'.join(stk)
