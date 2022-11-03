from pydantic import conint


class BankWallet:

    def __init__(self, amount: conint(gt=0)):
        self.balance = amount

    def deposit(self, amount: conint(gt=0)):
        self.balance += amount

    def debit(self, amount: conint(gt=0)):
        self.balance -= amount

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


w1 = BankWallet(10)
w2 = BankWallet(100)
w3 = BankWallet(-100)


print(w1)
print(w2)
print(w3)
