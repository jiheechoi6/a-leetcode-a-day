class UF:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
    
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        emailToAcc = {}

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                emailToAcc[email] = i
        
        emailMap = defaultdict(list)
        for email, owner in emailToAcc.items():
            emailMap[uf.find(owner)].append(email)
        
        return [[accounts[owner][0]] + sorted(emails) for owner, emails in emailMap.items()]
