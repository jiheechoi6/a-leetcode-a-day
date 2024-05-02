class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s)
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    sList[i] = ''
        
        for idx in stack:
            sList[idx] = ''

        return ''.join(sList)
      
