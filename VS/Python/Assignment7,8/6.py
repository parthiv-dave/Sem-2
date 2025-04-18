class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds or invalid amount")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")

account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, initial_balance)

while True:
    action = input("Choose action (deposit/withdraw/display/exit): ").strip().lower()
    if action == "deposit":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif action == "display":
        account.display()
    elif action == "exit":
        break
    else:
        print("Invalid action")