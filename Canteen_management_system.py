import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()    
window.title("Canteen Management APP")
window.geometry("750x450")
window.configure(bg="#87CEEB")

item_names = {
    "Burger-Rs50": 50, "Pizza-Rs100": 100, "Sandwich-Rs40": 40, "Pasta-Rs70": 70,
    "Coffee-Rs30": 30, "Tea-Rs20": 20, "Chips 1 plate-Rs50": 50, "Lays-Rs40": 40,
    "Cold Drink 1 ltr-Rs120": 120, "Sweets-Rs150": 150, "Juice-Rs100": 100,
    "Biryani 1 plate-Rs180": 180
}

item_list = list(item_names.keys())
order = []
 
label1 = tk.Label(window, text="<<<Canteen Management System>>>", font=("Helvetica", 20, "bold"), bg="#4682B4")
label1.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

label2 = tk.Label(window, text="Select an item:", bg="#87CEEB")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

combobox = ttk.Combobox(window, values=item_list)
combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label3 = tk.Label(window, text="Quantity:", bg="#87CEEB")
label3.grid(row=1, column=2, padx=10, pady=10, sticky="e")

entry1 = tk.Entry(window)
entry1.grid(row=1, column=3, padx=10, pady=10, sticky="w")

label4 = tk.Label(window, text="", bg="#87CEEB")
label4.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

listbox = tk.Listbox(window, width=50, height=10, font=("Helvetica", 12))
listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

def item_selected(event=None):
    selected_item = combobox.get()
    quantity = entry1.get()

    if selected_item not in item_names:
        messagebox.showwarning("Item Not Available", f"The item '{selected_item}' is not available.")
        return
    
    if selected_item and quantity:
        if quantity.isdigit():
            quantity = int(quantity)
            price = item_names[selected_item] * quantity
            order.append((selected_item, quantity, price))
            listbox.insert(tk.END, f"{selected_item} x {quantity} - PKR {price}")
            combobox.set('')
            entry1.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid integer quantity.")
button1 = tk.Button(window, text="Add to Order", command=item_selected, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
button1.grid(row=2, column=1, padx=10, pady=10)

def calculate_total():
    total = sum(price for item, quantity, price in order)
    messagebox.showinfo("Total Bill", f"Your total bill is: PKR {total}")

total_button = tk.Button(window, text="Calculate Total", command=calculate_total, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
total_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def reset_order():
    order.clear()
    listbox.delete(0, tk.END)

button3 = tk.Button(window, text="Reset Order", command=reset_order, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
button3.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

def delete_selected_item():
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        listbox.delete(selected_index)
        del order[selected_index]
    else:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")

button4 = tk.Button(window, text="Delete Selected Item", command=delete_selected_item, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
button4.grid(row=4, column=4, padx=10, pady=10)

combobox.bind("<<ComboboxSelected>>", item_selected)
window.mainloop()

