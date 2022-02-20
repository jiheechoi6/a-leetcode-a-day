class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        num = 0
        stk = []
        s += "/"
        
        for ch in s:
            # print(stk)
            if ch.isdigit():
                num = 10*num+int(ch)
            else:
                if ch==' ': continue
                elif sign=="+":   stk.append(num)
                elif sign=="-": stk.append(-num)
                elif sign=='*': stk.append(stk.pop()*num)
                elif sign=="/":
                    popped = stk.pop()
                    add = 0
                    if popped<0 and popped%num: add=1
                    stk.append(popped//num+add)
                num = 0
                
                sign = ch
        
        return sum(stk)
                
