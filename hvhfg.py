import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("300x150")
window.title("Table")
window.configure(bg="Sky Blue")

data = tk.IntVar()
val = ""

def hsn_table():
    global val
result = val
num = int(entry.get()) 

for i in range(1, 11):
    print(f"{num}x{i}={num*i}")
data.set("val")

frame = tk.Frame(window, bg='Blue')
frame.pack()

label = tk.Label(window, text="Enter number whose table you want to see:", fg='green')
label.pack()

entry = tk.Entry(window, fg="Blue", font=("Arial Black", 12))
entry.pack()

button = tk.Button(window, text="Submit", command=hsn_table)
button.pack()

window.mainloop()