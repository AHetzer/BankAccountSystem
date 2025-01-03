# Bank Account System with Tiered Interest Rates:

# A simple bank account system utilizing inheritance to create functionality for a regular bank account, savings account, and checking account.

# The savings account has a tiered interest system where if the account has $1000 or less the interest rate is 3%, 
# between $1000 and $5000 is 5%, and above $5000 is 7%.

# The checking account has a system where it charges an overdraft fee if the balance becomes negative when withdrawing. 
# However, you cannot go below the negative limit for balance.


class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'Account Holder: {self.name}\nBalance: ${round(self.balance,2)}'

class SavingsAccount(BankAccount):

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def apply_interest(self):  # Tiered interest rates
        if self.balance <= 1000:
            self.balance = self.balance*1.03
        elif self.balance <= 5000:
            self.balance = self.balance*1.05
        else:
            self.balance = self.balance*1.07


class CheckingAccount(BankAccount):
    NEGATIVE_BALANCE_LIMIT = -500   # Should be set to a negative number
    OVERDRAFT_FEE = 25              # Should be set to a positive number

    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.negative_bal_limit = self.NEGATIVE_BALANCE_LIMIT
        self.overdraft_fee = self.OVERDRAFT_FEE
    
    def withdraw(self, amount):
        if amount >= 0:
            if not self.balance - amount < self.negative_bal_limit: # Check to make sure we're not going under the limit
                self.balance = self.balance - amount
                if self.balance < 0:                      # Charging overdraft fee
                    self.balance -= self.overdraft_fee

