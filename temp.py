import tkinter as tk
from tkinter import messagebox
import json
import os

class BankAccount:
    def __init__(self, account_id, pin, balance=0):
        self.account_id = account_id
        self.pin = pin
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            self.history.append(f"Deposited: ${amount}")
            return f"Deposited: ${amount}. New balance: ${self.balance}"
        except ValueError as e:
            return f"Error: {e}"

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            if amount < 0:
                raise ValueError("Withdrawal amount must be positive.")
            self.balance -= amount
            self.history.append(f"Withdrew: ${amount}")
            return f"Withdrew: ${amount}. New balance: ${self.balance}"
        except ValueError as e:
            return f"Error: {e}"

    def get_history(self):
        return "\n".join(self.history)

    def reset_balance(self):
        self.balance = 0
        self.history.append("Balance reset")
        return "Balance has been reset to $0."

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history
        }

    @staticmethod
    def from_dict(data):
        account = BankAccount(data["account_id"], data["pin"], data["balance"])
        account.history = data["history"]
        return account

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Registration")
        self.root.geometry("400x300")
        self.root.configure(bg="#E0FFFF")

        self.label = tk.Label(root, text="Register an Account", font=("Helvetica", 18, "bold"), bg="#E0FFFF", fg="#4682B4")
        self.label.pack(pady=20)

        self.name_label = tk.Label(root, text="Account Number (12 digits):", font=("Helvetica", 14), bg="#E0FFFF", fg="#4682B4")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root, font=("Helvetica", 14))
        self.name_entry.pack(pady=5)
        self.name_entry.config(validate="key")
        self.name_entry.bind("<KeyRelease>", self.validate_name)

        self.pin_label = tk.Label(root, text="PIN (4 digits):", font=("Helvetica", 14), bg="#E0FFFF", fg="#4682B4")
        self.pin_label.pack(pady=5)
        self.pin_entry = tk.Entry(root, font=("Helvetica", 14), show='*')
        self.pin_entry.pack(pady=5)
        self.pin_entry.config(validate="key")
        self.pin_entry.bind("<KeyRelease>", self.validate_pin)

        self.show_pin_button = tk.Button(root, text="Show PIN", command=self.toggle_pin, font=("Helvetica", 14), bg="#87CEFA", fg="#000000")
        self.show_pin_button.pack(pady=5)

        self.register_button = tk.Button(root, text="Register", command=self.register, font=("Helvetica", 14), bg="#98FB98", fg="#000000")
        self.register_button.pack(pady=20)

        self.show_pin = False

    def validate_name(self, event):
        value = self.name_entry.get()
        if len(value) > 12 or not value.isdigit():
            self.name_entry.delete(len(value) - 1, tk.END)

    def validate_pin(self, event):
        value = self.pin_entry.get()
        if len(value) > 4 or not value.isdigit():
            self.pin_entry.delete(len(value) - 1, tk.END)

    def toggle_pin(self):
        if self.show_pin:
            self.pin_entry.config(show='*')
            self.show_pin_button.config(text="Show PIN")
        else:
            self.pin_entry.config(show='')
            self.show_pin_button.config(text="Hide PIN")
        self.show_pin = not self.show_pin

    def register(self):
        account_number = self.name_entry.get()
        pin = self.pin_entry.get()

        if not account_number or len(account_number) != 12:
            messagebox.showerror("Invalid Input", "Account number must be 12 digits.")
            return

        if not pin or len(pin) != 4:
            messagebox.showerror("Invalid Input", "PIN must be 4 digits.")
            return

        account_id = account_number
        account = BankAccount(account_id, pin)
        self.save_account(account)

        self.root.destroy()
        self.open_bank_app(account)

    def save_account(self, account):
        accounts = self.load_accounts()
        accounts[account.account_id] = account.to_dict()
        with open("accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

    @staticmethod
    def load_accounts():
        if not os.path.exists("accounts.json"):
            return {}
        with open("accounts.json", "r") as file:
            return json.load(file)

    def open_bank_app(self, account):
        bank_root = tk.Tk()
        BankApp(bank_root, account)
        bank_root.mainloop()

class BankApp:
    def __init__(self, root, account):
        self.account = account
        
        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("750x450")
        self.root.configure(bg="#E0FFFF")

        self.label = tk.Label(root, text="Bank Account Management", font=("Helvetica", 24, "bold"), bg="#E0FFFF", fg="#4682B4")
        self.label.pack(pady=20)
 
        self.amount_frame = tk.Frame(root, bg="#E0FFFF")
        self.amount_frame.pack(pady=10)

        self.amount_label = tk.Label(self.amount_frame, text="Amount:", font=("Helvetica", 14), bg="#E0FFFF", fg="#4682B4")
        self.amount_label.grid(row=0, column=0, padx=10)

        self.amount_entry = tk.Entry(self.amount_frame, font=("Helvetica", 14))
        self.amount_entry.grid(row=0, column=1, padx=10)

        self.button_frame = tk.Frame(root, bg="#E0FFFF")
        self.button_frame.pack(pady=10)

        self.deposit_button = tk.Button(self.button_frame, text="Deposit", command=self.deposit, font=("Helvetica", 14), bg="#98FB98", fg="#000000")
        self.deposit_button.grid(row=0, column=0, padx=10)

        self.withdraw_button = tk.Button(self.button_frame, text="Withdraw", command=self.withdraw, font=("Helvetica", 14), bg="#FFB6C1", fg="#000000")
        self.withdraw_button.grid(row=0, column=1, padx=10)

        self.history_button = tk.Button(self.button_frame, text="View Transaction History", command=self.view_history, font=("Helvetica", 14), bg="#87CEFA", fg="#000000")
        self.history_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset Balance", command=self.reset_balance, font=("Helvetica", 14), bg="#FF6347", fg="#FFFFFF")
        self.reset_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.balance_label = tk.Label(root, text=f"Current Balance: ${self.account.balance}", font=("Helvetica", 16), bg="#E0FFFF", fg="#4682B4")
        self.balance_label.pack(pady=20)

    def deposit(self):
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            result = self.account.deposit(amount)
            self.save_account()
            messagebox.showinfo("Deposit", result)
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
        
    def withdraw(self):
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            result = self.account.withdraw(amount)
            self.save_account()
            messagebox.showinfo("Withdraw", result)
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def view_history(self):
        history = self.account.get_history()
        if history:
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions yet.")
    
    def reset_balance(self):
        result = self.account.reset_balance()
        self.save_account()
        messagebox.showinfo("Reset Balance", result)
        self.update_balance()

    def update_balance(self):
        self.balance_label.config(text=f"Current Balance: ${self.account.balance}")

    def save_account(self):
        accounts = RegistrationApp.load_accounts()
        accounts[self.account.account_id] = self.account.to_dict()
        with open("accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()
