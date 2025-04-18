class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}")

account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
account = BankAccount(account_number, name)

while True:
    action = input("Enter 'deposit', 'withdraw', 'balance', or 'exit': ").strip().lower()
    if action == 'deposit':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif action == 'balance':
        account.display_balance()
    elif action == 'exit':
        break
    else:
        print("Invalid input. Try again.")
