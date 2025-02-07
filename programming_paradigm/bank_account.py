class BankAccount:
    def __init__(self,initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount

        else :
            print("Enter a +ve value")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount < 0 :
            print("Amount should be a positive number")
            return False
        else :
            print("Insufficient funds")
            return False

    def display(self):
        print(f"Current balance: ${self.account_balance}")
        
