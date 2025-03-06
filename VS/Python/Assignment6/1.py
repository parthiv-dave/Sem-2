class Password_manager:
    def __init__(self):
        self.old_passwords = []
    
    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password updated successfully.")
        else:
            print("Error: Password has been used before. Choose a different password.")
    
    def is_correct(self, password):
        return password == self.get_password()

manager = Password_manager()
while True:
    action = input("Enter 'set' to set a password, 'check' to verify a password, or 'exit' to quit: ").strip().lower()
    if action == 'set':
        new_password = input("Enter new password: ")
        manager.set_password(new_password)
    elif action == 'check':
        check_password = input("Enter password to check: ")
        if manager.is_correct(check_password):
            print("Password is correct.")
        else:
            print("Incorrect password.")
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please try again.")
