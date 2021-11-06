class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ispositive = (dividend>0) is (divisor>0)
        dividend, divisor = abs(dividend), abs(divisor) 
        
        cur_divisor = divisor
        answer = 0
        while dividend>=divisor:
            cur_ans = 1
            while cur_divisor<<1 <= dividend:
                cur_divisor<<=1
                cur_ans<<=1
            dividend -= cur_divisor
            answer += cur_ans
            cur_divisor = divisor
        
        if not ispositive: answer = -answer
        return min(max(answer, -2147483648), 2147483647)
        
