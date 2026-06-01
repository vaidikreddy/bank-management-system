import json
import os


class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance:.2f}")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return BankAccount(
            data["account_number"],
            data["name"],
            data["balance"]
        )


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.file_name = "accounts.json"
        self.load_accounts()

    def create_account(self):
        account_number = input("Enter Account Number: ")

        if account_number in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter Account Holder Name: ")

        try:
            balance = float(input("Enter Initial Deposit: "))
        except ValueError:
            print("Invalid amount.")
            return

        self.accounts[account_number] = BankAccount(
            account_number,
            name,
            balance
        )

        self.save_accounts()
        print("Account created successfully.")

    def view_account(self):
        account_number = input("Enter Account Number: ")

        account = self.accounts.get(account_number)

        if account:
            account.display()
        else:
            print("Account not found.")

    def deposit_money(self):
        account_number = input("Enter Account Number: ")

        account = self.accounts.get(account_number)

        if not account:
            print("Account not found.")
            return

        try:
            amount = float(input("Enter Amount to Deposit: "))
            account.deposit(amount)
            self.save_accounts()
        except ValueError:
            print("Invalid amount.")

    def withdraw_money(self):
        account_number = input("Enter Account Number: ")

        account = self.accounts.get(account_number)

        if not account:
            print("Account not found.")
            return

        try:
            amount = float(input("Enter Amount to Withdraw: "))
            account.withdraw(amount)
            self.save_accounts()
        except ValueError:
            print("Invalid amount.")

    def save_accounts(self):
        data = {
            acc_no: account.to_dict()
            for acc_no, account in self.accounts.items()
        }

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def load_accounts(self):
        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, "r") as file:
            data = json.load(file)

            for acc_no, acc_data in data.items():
                self.accounts[acc_no] = BankAccount.from_dict(acc_data)

    def menu(self):
        while True:
            print("\n===== BANK MANAGEMENT SYSTEM =====")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.view_account()

            elif choice == "3":
                self.deposit_money()

            elif choice == "4":
                self.withdraw_money()

            elif choice == "5":
                print("Thank you for using the Bank Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.menu()