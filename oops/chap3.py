class BankAccount:
    def __init__(self):
        self._balance = 0.0 ## Encapsulated data, protected
    
    @property
    def balance(self): ## Controlled access to balance
        """Getter for balance property"""
        return self._balance
    
    def deposit(self,amount):
        """Method to deposit money into the account"""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")
    def withdraw(self,amount):
        """Method to withdraw money from the account"""
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")
        
bank1 = BankAccount()
bank1.deposit(1000)
bank1.deposit(200)
bank1.deposit(100)
print(bank1.balance)