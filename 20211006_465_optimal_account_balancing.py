class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        self.credits = collections.defaultdict(int)
        self.min_trx = math.inf
        for giver, receiver, amt in transactions:
            self.credits[giver] -= amt
            self.credits[receiver] += amt
            
        ppl_lst = [usr for usr, amt in self.credits.items() if amt!=0]
        
        self.backtrack(ppl_lst, 0)
        return self.min_trx
    
    def backtrack(self, ppl_lst, cur_trx):
        if len(ppl_lst)<=1: 
            self.min_trx = cur_trx
            return
        if self.credits[ppl_lst[0]]==0:   self.backtrack(ppl_lst[1:], cur_trx)
        if cur_trx >= self.min_trx:  return
        
        for usr in ppl_lst[1:]:
            if self.credits[usr]*self.credits[ppl_lst[0]]<0:
                self.credits[usr] += self.credits[ppl_lst[0]]
                self.backtrack(ppl_lst[1:], cur_trx+1)
                self.credits[usr] -= self.credits[ppl_lst[0]]

            
