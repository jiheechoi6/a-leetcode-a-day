class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        s = s+'+'
        stk = []
        prev_op = '+'

        for ch in s:
            if ch == ' ':
                pass
            elif ch.isdigit():
                num = num*10 + int(ch)
            else:
                if prev_op == '+':
                    stk.append(num)
                elif prev_op == '-':
                    stk.append(-num)
                elif prev_op == '*':
                    pre_num = stk.pop()
                    stk.append(pre_num*num)
                elif prev_op == '/':
                    stk.append(math.trunc(stk.pop()/num))
                num = 0
                prev_op = ch
        return sum(stk)
        
