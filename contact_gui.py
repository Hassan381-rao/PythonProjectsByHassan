import tkinter as tk
from tkinter import messagebox

contacts = [
    {'name': 'Hassan', 'ID': '095-1111', 'Phone': '+92454813812', 'email': 'ABDURRAHMAN@gmail.com', 'address': 'XYZ'},
    {'name': 'Sameed', 'ID': '095-4224', 'Phone': '+923123716235', 'email': 'SAMEED@gmail.com', 'address': 'XYZ'},
    {'name': 'Umar', 'ID': '095-3243', 'Phone': '+921988816232', 'email': 'UMAR@gmail.com', 'address': 'XYZ'},
    {'name': 'Shoaib', 'ID': '095-5432', 'Phone': '+923478814234', 'email': 'SHOAIB@gmail.com', 'address': 'XYZ'},
    {'name': 'Danial', 'ID': '095-2433', 'Phone': '+923638816214', 'email': 'DANIAL@gmail.com', 'address': 'XYZ'},
    {'name': 'Bilal', 'ID': '095-7953', 'Phone': '+923313216437', 'email': 'BILAL@gmail.com', 'address': 'XYZ'},
    {'name': 'Asim', 'ID': '095-2345', 'Phone': '+923372346232', 'email': 'ASIM@gmail.com', 'address': 'XYZ'},
    {'name': 'Rasheed', 'ID': '095-1734', 'Phone': '+9213478816236', 'email': 'RASHEED@gmail.com', 'address': 'XYZ'},
    {'name': 'Imran', 'ID': '095-1937', 'Phone': '+923371816230', 'email': 'IMRAN@gmail.com', 'address': 'XYZ'},
    {'name': 'Ali', 'ID': '095-9378', 'Phone': '+923873416137', 'email': 'ALI@gmail.com', 'address': 'XYZ'}
]

def search_contacts():
    search_term = entry.get().strip().lower()
    found_contacts = [c for c in contacts if (c['name'].strip().lower() == search_term or c['Phone'].strip().lower() == search_term)]
    
    if found_contacts:
        result = ""
        for c in found_contacts:
            result += f"Name: {c['name']}\nID: {c['ID']}\nPhone: {c['Phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n\n"
        messagebox.showinfo("Your Contact", result)
    else:
        messagebox.showerror("Error", "No contact found with that Name or Phone Number")


root = tk.Tk()
root.title("Contact Management System")
root.configure(bg="Sky Blue")

label = tk.Label(root, text="<<< Contact Management System >>>", bg="Sky Blue", fg="blue", font=("Helvetica", 16, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)

entry_label = tk.Label(root, text="Enter Name or Phone Number:", bg="Sky Blue", fg="black")
entry_label.grid(row=1, column=0, pady=5)

entry = tk.Entry(root, bg="white", fg="black")
entry.grid(row=1, column=1, pady=5)

search_button = tk.Button(root, text="Search", command=search_contacts, bg="#4CAF50", fg="white", activebackground="#45a049")
search_button.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
