class Solution:
    answer = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.createOne(0, 0, '', n)
        return self.answer
    
    def createOne(self, openp, closep, p, n):
        if openp < n: self.createOne(openp+1, closep, p+'(', n)
        if closep < openp: self.createOne(openp, closep+1, p+')', n)
        if closep == n: self.answer.append(p)
