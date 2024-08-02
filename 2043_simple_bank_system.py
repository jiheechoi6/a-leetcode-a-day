class Bank:
    def __init__(self, balance: List[int]):
        self.balances = [0] + balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._isAccountValid(account1) or not self._isAccountValid(account2):
            return False
        if self.balances[account1] < money: return False

        self.balances[account1] -= money
        self.balances[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._isAccountValid(account): return False

        self.balances[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._isAccountValid(account): return False
        if self.balances[account] < money: return False

        self.balances[account] -= money
        return True

    def _isAccountValid(self, account: int) -> bool:
        if 1 > account or account > self.n: return False
        else: return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
