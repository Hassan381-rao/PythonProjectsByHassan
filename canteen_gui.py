import tkinter as tk
from tkinter import messagebox
from datetime import date


menu_items = {
    "Burger": 50,
    "Pizza": 100,
    "Sandwich": 40,
    "Pasta": 70,
    "Coffee": 30,
    "Tea": 20,
}


root = tk.Tk()
root.title("Canteen Management System")
root.geometry("400x400")
root.configure(bg="sky blue")

order = {}

def add_to_order(item):
    if item in order:
        order[item] += 1
    else:
        order[item] = 1
    update_order_display()

def update_order_display():
    order_text.config(state=tk.NORMAL)
    order_text.delete(1.0, tk.END)
    total_cost = 0
    for item, quantity in order.items():
        cost = menu_items[item] * quantity
        order_text.insert(tk.END, f"{item} x{quantity} - Rs{cost}\n")
        total_cost += cost
    order_text.insert(tk.END, f"\nTotal Cost: Rs{total_cost}")
    order_text.config(state=tk.DISABLED)

def finalize_order():
    if not order:
        messagebox.showinfo("Order Status", "Your order is empty!")
    else:
        messagebox.showinfo("Order Status", "Order placed successfully!")
        order.clear()
        update_order_display()

menu_frame = tk.Frame(root, bg="Sky blue")
menu_frame.pack(pady=10)

tk.Label(root)
tk.Label(menu_frame, text="Menu", font=("Helvetica", 20, "bold"), bg="Sky blue").pack()

for item, price in menu_items.items():
    button = tk.Button(menu_frame, text=f"{item} - Rs{price}", command=lambda item=item: add_to_order(item))
    button.pack(pady=5)

order_frame = tk.Frame(root, bg="Sky blue")
order_frame.pack(pady=10)

tk.Label(order_frame, text="Order", font=("Helvetica", 16, "bold"), bg="Sky blue").pack()

order_text = tk.Text(order_frame, width=40, height=10, state=tk.DISABLED, bg="Sky blue")
order_text.pack(pady=5)

finalize_button = tk.Button(root, text="Finalize Order", command=finalize_order, bg="Sky blue", fg="black", font=("Helvetica", 12, "bold"))
finalize_button.pack(pady=20)

root.mainloop()
