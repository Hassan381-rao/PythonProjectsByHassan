class BankAccount:
    def __init__(self, balance=0):
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

def main():
    account = BankAccount()

    while True:
        print("\nBank Account Management System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. Reset Balance")
        print("5. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == "3":
            print("Transaction History:")
            print(account.get_history())
        elif choice == "4":
            print(account.reset_balance())
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
