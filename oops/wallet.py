class Wallet:
    def __init__(self):
        self.__balance = 0
    def __validate(self,amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount
    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient fund")
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
    
acct_one = Wallet()
acct_one.deposit(4)
print(acct_one.get_balance())

acct_one.deposit(50)
print(acct_one.get_balance())
acct_one.withdraw(8)
acct_one.withdraw(58)