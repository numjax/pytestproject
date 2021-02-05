class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Not enough balance.")

    def deposit(self, amount):
        self.balance += amount


    def __str__(self):
        return "{}, your balance is {}".format(self.name, self.balance)


class CheckingAccount(BankAccount):
    def __init__(self, name, balance, max_spending):
        super().__init__(name, balance)
        self.max_spending = max_spending


    def use_check_card(self, amount):
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print ("{}, exceed the limit {}.".format(self.name, self.max_spending))


class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance *= (self.interest_rate+1)

bank_account1 = CheckingAccount("Teaho", 100000, 10000)
bank_account2 = SavingsAccount("Young", 20000, 0.05)

bank_account1.withdraw (1000)
bank_account1.deposit(1000)
bank_account1.use_check_card(2000)

bank_account2.withdraw (1000)
bank_account2.deposit (1000)
bank_account2.add_interest()


print (bank_account1)
print (bank_account2)

print (CheckingAccount.mro())
print (SavingsAccount.mro())
