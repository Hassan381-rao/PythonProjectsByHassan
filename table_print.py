import tkinter as tk
window=tk.Tk()
window.geometry("300x250")
window.title("Table")
window.configure(bg="Sky Blue")


def hsn_table():
    try:
        num = int(entry.get())
        result = ""
        for i in range(1, 11):
            result += f"{num} x {i} = {num * i}\n"
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Please enter a valid number")
        
frame = tk.Frame(window, bg='Sky Blue')
frame.grid(row=0, column=0, padx=10, pady=10)

label = tk.Label(frame, text="Enter number whose table you want to see:", fg='green', bg='Sky Blue')
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, fg="Blue", font=("Arial Black", 12))
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(frame, text="Submit", command=hsn_table)
button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="", bg='Sky Blue', fg='Black', font=("Arial", 12))
result_label.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()

