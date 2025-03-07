
import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(window, balance=0):
        window.balance = balance
        window.history = []

    def deposit(window, amount):
        try:
            if amount < 0:
                raise ValueError("Deposit amount must be positive.")
            window.balance += amount
            window.history.append(f"Deposited: ${amount}")
            return f"Deposited: ${amount}. New balance: ${window.balance}"
        except ValueError as e:
            return f"Error: {e}"

    def withdraw(window, amount):
        try:
            if amount > window.balance:
                raise ValueError("Insufficient funds.")
            if amount < 0:
                raise ValueError("Withdrawal amount must be positive.")
            window.balance -= amount
            window.history.append(f"Withdrew: ${amount}")
            return f"Withdrew: ${amount}. New balance: ${window.balance}"
        except ValueError as e:
            return f"Error: {e}"

    def get_history(window):
        return "\n".join(window.history)

    def reset_balance(window):
        window.balance = 0
        window.history.append("Balance reset")
        return "Balance has been reset to $0."

class BankApp:
    def __init__(window, root):
        window.account = BankAccount()
        
        window.root = root
        window.root.title("Banking Management System")
        window.root.geometry("750x450")
        window.root.configure(bg="#E0FFFF")  

        window.label = tk.Label(root, text="Bank Account Management", font=("Helvetica", 24, "bold"), bg="#E0FFFF", fg="#4682B4")
        window.label.pack(pady=20)
 
        window.amount_frame = tk.Frame(root, bg="#E0FFFF")
        window.amount_frame.pack(pady=10)

        window.amount_label = tk.Label(window.amount_frame, text="Amount:", font=("Helvetica", 14), bg="#E0FFFF", fg="#4682B4")
        window.amount_label.grid(row=0, column=0, padx=10)

        window.amount_entry = tk.Entry(window.amount_frame, font=("Helvetica", 14))
        window.amount_entry.grid(row=0, column=1, padx=10)

        window.button_frame = tk.Frame(root, bg="#E0FFFF")
        window.button_frame.pack(pady=10)

        window.deposit_button = tk.Button(window.button_frame, text="Deposit", command=window.deposit, font=("Helvetica", 14), bg="#98FB98", fg="#000000")
        window.deposit_button.grid(row=0, column=0, padx=10)

        window.withdraw_button = tk.Button(window.button_frame, text="Withdraw", command=window.withdraw, font=("Helvetica", 14), bg="#FFB6C1", fg="#000000")
        window.withdraw_button.grid(row=0, column=1, padx=10)

        window.history_button = tk.Button(window.button_frame, text="View Transaction History", command=window.view_history, font=("Helvetica", 14), bg="#87CEFA", fg="#000000")
        window.history_button.grid(row=1, column=0, columnspan=2, pady=10)

        window.reset_button = tk.Button(window.button_frame, text="Reset Balance", command=window.reset_balance, font=("Helvetica", 14), bg="#FF6347", fg="#FFFFFF")
        window.reset_button.grid(row=2, column=0, columnspan=2, pady=10)

        window.balance_label = tk.Label(root, text=f"Current Balance: ${window.account.balance}", font=("Helvetica", 16), bg="#E0FFFF", fg="#4682B4")
        window.balance_label.pack(pady=20)

    def deposit(window):
        amount_str = window.amount_entry.get()
        try:
            amount = float(amount_str)
            result = window.account.deposit(amount)
            messagebox.showinfo("Deposit", result)
            window.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
        
    def withdraw(window):
        amount_str = window.amount_entry.get()
        try:
            amount = float(amount_str)
            result = window.account.withdraw(amount)
            messagebox.showinfo("Withdraw", result)
            window.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def view_history(window):
        history = window.account.get_history()
        if history:
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions yet.")
    
    def reset_balance(window):
        result = window.account.reset_balance()
        messagebox.showinfo("Reset Balance", result)
        window.update_balance()

    def update_balance(window):
        window.balance_label.config(text=f"Current Balance: ${window.account.balance}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
