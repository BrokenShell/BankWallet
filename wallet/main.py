from pydantic import conint


class BankWallet:
    # Todo: Add overdraft charge logic

    def __init__(self, amount: conint(gt=0)):
        #Todo: Protect from negative amounts
        self.balance = amount

    def deposit(self, amount: conint(gt=0)):
        # Todo: Protect from negative amounts
        self.balance += amount

    def debit(self, amount: conint(gt=0)):
        # Todo: Protect from negative amounts
        self.balance -= amount

    def __str__(self):
        return "\n".join(f"{k} => {v}" for k, v in vars(self).items())

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.balance < other.balance


w1 = BankWallet(10)
w2 = BankWallet(100)
w3 = BankWallet(-100)
arr = [w1, w2, w3]
arr.sort()
print(arr)
