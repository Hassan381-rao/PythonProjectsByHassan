import tkinter as tk
from tkinter import messagebox

def display_menu():
    menu = """
Phone Book Menu:
1. View Contacts
2. Add Contact
3. Update Contact
4. Delete Contact
5. Search Contact
6. Exit
"""
    print(menu)

def view_contacts(phone_book):
    contacts = ""
    if not phone_book:
        contacts = "No contacts found."
    else:
        for name, number in phone_book.items():
            contacts += f"Name: {name}, Number: {number}\n"
    messagebox.showinfo("Contacts", contacts)

def add_contact(phone_book, name_entry, number_entry):
    name = name_entry.get()
    number = number_entry.get()
    if name in phone_book:
        messagebox.showerror("Error", "Contact already exists.")
    else:
        phone_book[name] = number
        messagebox.showinfo("Success", "Contact added successfully.")
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

def update_contact(phone_book, name_entry, number_entry):
    name = name_entry.get()
    number = number_entry.get()
    if name in phone_book:
        phone_book[name] = number
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showerror("Error", "Contact not found.")
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

def delete_contact(phone_book, name_entry):
    name = name_entry.get()
    if name in phone_book:
        del phone_book[name]
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "Contact not found.")
    name_entry.delete(0, tk.END)

def search_contact(phone_book, name_entry):
    name = name_entry.get()
    if name in phone_book:
        messagebox.showinfo("Contact Found", f"Name: {name}, Number: {phone_book[name]}")
    else:
        messagebox.showerror("Error", "Contact not found.")
    name_entry.delete(0, tk.END)

def main():
    phone_book = {}

    root = tk.Tk()
    root.title("Phone Book")
    root.configure(bg="Sky Blue")  

    tk.Label(root, text="Name:", bg="Sky Blue").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Number:", bg="Sky Blue").grid(row=1, column=0, padx=10, pady=5)

    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    number_entry = tk.Entry(root)
    number_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="View Contacts", command=lambda: view_contacts(phone_book), bg="sky blue", fg="white").grid(row=2, column=0, padx=10, pady=5)
    tk.Button(root, text="Add Contact", command=lambda: add_contact(phone_book, name_entry, number_entry), bg="sky blue", fg="white").grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Update Contact", command=lambda: update_contact(phone_book, name_entry, number_entry), bg="sky blue", fg="white").grid(row=3, column=0, padx=10, pady=5)
    tk.Button(root, text="Delete Contact", command=lambda: delete_contact(phone_book, name_entry), bg="sky blue", fg="white").grid(row=3, column=1, padx=10, pady=5)
    tk.Button(root, text="Search Contact", command=lambda: search_contact(phone_book, name_entry), bg="sky blue", fg="white").grid(row=4, column=0, padx=10, pady=5)
    tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white").grid(row=4, column=1, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
