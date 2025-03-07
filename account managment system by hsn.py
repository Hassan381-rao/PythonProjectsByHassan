import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random

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
            if amount < 500:
                raise ValueError("Minimum withdrawal amount is $500.")
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

class RegistrationWindow:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.window = tk.Toplevel(root)
        self.window.title("Register Account")
        self.window.geometry("400x300")
        self.window.configure(bg="#34495E")

        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Arial", 12, "bold"),
                        padding=10,
                        relief="flat",
                        background="#16A085",
                        foreground="white")
        style.configure("Custom.TLabel",
                        font=("Arial", 12, "bold"),
                        background="#34495E",
                        foreground="white")
        style.configure("Custom.TEntry",
                        font=("Arial", 12))

        self.label = tk.Label(self.window, text="Register Account", font=("Arial", 16, "bold"), bg="#34495E", fg="white")
        self.label.pack(pady=20)

        self.name_label = tk.Label(self.window, text="Name:", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.window, font=("Arial", 12, "bold"))
        self.name_entry.pack(pady=5, padx=20, fill='x')

        self.phone_label = tk.Label(self.window, text="Phone Number:", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.window, font=("Arial", 12, "bold"))
        self.phone_entry.pack(pady=5, padx=20, fill='x')

        self.id_card_label = tk.Label(self.window, text="ID Card Number:", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.id_card_label.pack(pady=5)
        self.id_card_entry = tk.Entry(self.window, font=("Arial", 12, "bold"))
        self.id_card_entry.pack(pady=5, padx=20, fill='x')

        self.pin_label = tk.Label(self.window, text="PIN (4 digits):", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.pin_label.pack(pady=5)
        self.pin_entry = tk.Entry(self.window, font=("Arial", 12, "bold"), show='*')
        self.pin_entry.pack(pady=5, padx=20, fill='x')

        self.show_pin_button = tk.Button(self.window, text="Show PIN", command=self.toggle_pin, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.show_pin_button.pack(pady=5)

        self.register_button = tk.Button(self.window, text="Register", command=self.register, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.register_button.pack(pady=10)

        self.show_pin = False

    def toggle_pin(self):
        if self.show_pin:
            self.pin_entry.config(show='*')
            self.show_pin_button.config(text="Show PIN")
        else:
            self.pin_entry.config(show='')
            self.show_pin_button.config(text="Hide PIN")
        self.show_pin = not self.show_pin

    def register(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        id_card_number = self.id_card_entry.get()
        pin = self.pin_entry.get()

        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Invalid Input", "PIN must be 4 digits.")
            return

        account_number = self.generate_account_number()
        account_id = account_number
        account = BankAccount(account_id, pin)
        self.callback(account, name, phone_number, id_card_number)
        self.window.destroy()

    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])

class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Management")
        self.root.geometry("400x400")
        self.root.configure(bg="#34495E")

        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Arial", 12, "bold"),
                        padding=10,
                        relief="flat",
                        background="#16A085",
                        foreground="white")
        style.configure("Custom.TLabel",
                        font=("Arial", 12, "bold"),
                        background="#34495E",
                        foreground="white")
        style.configure("Custom.TEntry",
                        font=("Arial", 12))

        self.label = tk.Label(root, text="Account Management", font=("Arial", 16, "bold"), bg="#34495E", fg="white")
        self.label.pack(pady=20)

        self.account_label = tk.Label(root, text="Account Number (12 digits):", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.account_label.pack(pady=5)
        self.account_entry = tk.Entry(root, font=("Arial", 12, "bold"))
        self.account_entry.pack(pady=5, padx=20, fill='x')

        self.pin_label = tk.Label(root, text="PIN (4 digits):", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.pin_label.pack(pady=5)
        self.pin_entry = tk.Entry(root, font=("Arial", 12, "bold"), show='*')
        self.pin_entry.pack(pady=5, padx=20, fill='x')

        self.show_pin_button = tk.Button(root, text="Show PIN", command=self.toggle_pin, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.show_pin_button.pack(pady=5)

        self.register_button = tk.Button(root, text="Register", command=self.open_registration_window, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.register_button.pack(pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.login_button.pack(pady=10)

        self.show_pin = False

    def toggle_pin(self):
        if self.show_pin:
            self.pin_entry.config(show='*')
            self.show_pin_button.config(text="Show PIN")
        else:
            self.pin_entry.config(show='')
            self.show_pin_button.config(text="Hide PIN")
        self.show_pin = not self.show_pin

    def open_registration_window(self):
        RegistrationWindow(self.root, self.register_account)

    def register_account(self, account, name, phone_number, id_card_number):
        self.save_account(account, name, phone_number, id_card_number)
        messagebox.showinfo("Registration Successful", "Account registered successfully!")
        self.reset_fields()

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()

        accounts = self.load_accounts()
        account_data = accounts.get(account_number)

        if not account_data:
            messagebox.showerror("Login Failed", "Account not found.")
            return

        if account_data["pin"] != pin:
            messagebox.showerror("Login Failed", "Incorrect PIN.")
            return

        account = BankAccount.from_dict(account_data)
        self.root.destroy()
        new_root = tk.Tk()
        BankApp(new_root, account)
        new_root.mainloop()

    def save_account(self, account, name, phone_number, id_card_number):
        accounts = self.load_accounts()
        accounts[account.account_id] = {
            **account.to_dict(),
            "name": name,
            "phone_number": phone_number,
            "id_card_number": id_card_number
        }
        with open("accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

    def load_accounts(self):
        if not os.path.exists("accounts.json"):
            return {}
        with open("accounts.json", "r") as file:
            return json.load(file)

    def reset_fields(self):
        self.account_entry.delete(0, tk.END)
        self.pin_entry.delete(0, tk.END)

class BankApp:
    def __init__(self, root, account):
        self.account = account

        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("800x450")
        self.root.configure(bg="#34495E")

        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Arial", 12, "bold"),
                        padding=10,
                        relief="flat",
                        background="#16A085",
                        foreground="white")
        style.configure("Custom.TLabel",
                        font=("Arial", 14, "bold"),
                        background="#34495E",
                        foreground="white")
        style.configure("Custom.TEntry",
                        font=("Arial", 12))
        style.configure("Custom.TFrame",
                        background="#34495E")

        self.main_frame = tk.Frame(root, bg="#34495E")
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Bank Account Management", font=("Arial", 16, "bold"), bg="#34495E", fg="white")
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.balance_label = tk.Label(self.main_frame, text=f"Current Balance: ${self.account.balance}", font=("Arial", 14, "bold"), bg="#34495E", fg="white")
        self.balance_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self.amount_label = tk.Label(self.main_frame, text="Amount:", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.amount_entry = tk.Entry(self.main_frame, font=("Arial", 12, "bold"))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.deposit_button = tk.Button(self.main_frame, text="Deposit", command=self.deposit, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.deposit_button.grid(row=3, column=0, padx=10, pady=10)

        self.withdraw_button = tk.Button(self.main_frame, text="Withdraw", command=self.withdraw, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.withdraw_button.grid(row=3, column=1, padx=10, pady=10)

        self.history_button = tk.Button(self.main_frame, text="View Transaction History", command=self.view_history, font=("Arial", 12, "bold"), bg="#16A085", fg="white")
        self.history_button.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        self.amount_buttons_frame = tk.Frame(root, bg="#34495E")
        self.amount_buttons_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

        self.amounts = [500, 1000, 5000, 25000, 50000]
        for amount in self.amounts:
            button = tk.Button(self.amount_buttons_frame, text=f"${amount}", command=lambda amt=amount: self.add_amount(amt), font=("Arial", 12, "bold"), bg="#16A085", fg="white")
            button.pack(pady=5, padx=10, fill=tk.X)

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

    def add_amount(self, amount):
        try:
            current_text = self.amount_entry.get()
            current_amount = float(current_text) if current_text else 0
            new_amount = current_amount + amount
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, f"{new_amount:.2f}")
        except ValueError:
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, f"{amount:.2f}")

    def save_account(self):
        accounts = RegistrationApp.load_accounts()
        accounts[self.account.account_id] = self.account.to_dict()
        with open("accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()     