import pandas as pd
from getpass import getpass
import json
import os

# File to store user data
DATA_FILE = 'bank_users.csv'

# Load data from file if exists
if os.path.exists(DATA_FILE):
    users_df = pd.read_csv(DATA_FILE)
    users_df['history'] = users_df['history'].apply(json.loads)  # Convert history back to list
else:
    users_df = pd.DataFrame(columns=['userid', 'password', 'balance', 'history'])

def save_data():
    users_df_copy = users_df.copy()
    users_df_copy['history'] = users_df_copy['history'].apply(json.dumps)  # Convert list to string
    users_df_copy.to_csv(DATA_FILE, index=False)

def register():
    userid = input("Choose a user ID: ")
    if userid in users_df['userid'].values:
        print("❌ User ID already exists!")
        return
    password = getpass("Choose a password: ")
    users_df.loc[len(users_df)] = [userid, password, 0.0, []]
    save_data()
    print("✅ Registration successful!")

def login():
    userid = input("User ID: ")
    password = getpass("Password: ")
    user_row = users_df[(users_df['userid'] == userid) & (users_df['password'] == password)]
    if not user_row.empty:
        print(f"🔓 Welcome, {userid}!")
        return user_row.index[0]  # return index
    else:
        print("❌ Invalid credentials.")
        return None

def deposit(user_idx):
    amount = float(input("Enter deposit amount: ₹"))
    users_df.at[user_idx, 'balance'] += amount
    users_df.at[user_idx, 'history'].append(f"Deposited ₹{amount}")
    save_data()
    print(f"✅ ₹{amount} deposited. New Balance: ₹{users_df.at[user_idx, 'balance']}")

def withdraw(user_idx):
    amount = float(input("Enter withdrawal amount: ₹"))
    if users_df.at[user_idx, 'balance'] >= amount:
        users_df.at[user_idx, 'balance'] -= amount
        users_df.at[user_idx, 'history'].append(f"Withdrew ₹{amount}")
        save_data()
        print(f"✅ ₹{amount} withdrawn. New Balance: ₹{users_df.at[user_idx, 'balance']}")
    else:
        print("❌ Insufficient balance.")

def transfer(user_idx):
    receiver_id = input("Enter receiver User ID: ")
    if receiver_id not in users_df['userid'].values:
        print("❌ Receiver not found.")
        return
    amount = float(input("Enter amount to transfer: ₹"))
    if users_df.at[user_idx, 'balance'] >= amount:
        receiver_idx = users_df[users_df['userid'] == receiver_id].index[0]
        users_df.at[user_idx, 'balance'] -= amount
        users_df.at[receiver_idx, 'balance'] += amount
        sender_id = users_df.at[user_idx, 'userid']
        users_df.at[user_idx, 'history'].append(f"Transferred ₹{amount} to {receiver_id}")
        users_df.at[receiver_idx, 'history'].append(f"Received ₹{amount} from {sender_id}")
        save_data()
        print(f"✅ ₹{amount} transferred to {receiver_id}.")
    else:
        print("❌ Insufficient balance.")

def show_balance(user_idx):
    print(f"💰 Current Balance: ₹{users_df.at[user_idx, 'balance']}")

def transaction_history(user_idx):
    print("📜 Transaction History:")
    for item in users_df.at[user_idx, 'history']:
        print(f" - {item}")

def main_menu():
    while True:
        print("\n🏦 Welcome to Python Bank")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            user_idx = login()
            if user_idx is not None:
                user_menu(user_idx)
        elif choice == '3':
            print("👋 Thank you for using Python Bank!")
            break
        else:
            print("❗ Invalid option.")

def user_menu(user_idx):
    while True:
        print("\n💼 User Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Transaction History")
        print("6. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            deposit(user_idx)
        elif choice == '2':
            withdraw(user_idx)
        elif choice == '3':
            transfer(user_idx)
        elif choice == '4':
            show_balance(user_idx)
        elif choice == '5':
            transaction_history(user_idx)
        elif choice == '6':
            print("🔒 Logged out.")
            break
        else:
            print("❗ Invalid option.")

# Run the app
main_menu()
