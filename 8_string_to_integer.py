class Solution:
    def myAtoi(self, s: str) -> int:
        sign, res, i = 1, 0, 0

        # skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-': sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i+= 1
        
        return min(2**31-1, max(sign*res, -2**31))
