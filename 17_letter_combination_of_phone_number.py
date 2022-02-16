class Solution:
    m = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        ans = ['']
        for num in digits:
            temp = []
            for ch in self.m[int(num)]:
                for elem in ans:
                    temp.append(elem+ch)
            ans = temp
                    
        return ans
