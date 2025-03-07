import tkinter as tk
from tkinter import messagebox

def create_result_card(student_name, subjects, marks):
    
    header = f"Result Card for {student_name}"
    underline = "-" * len(header)
    
   
    result_lines = []
    for subject, mark in zip(subjects, marks):
        result_lines.append(f"{subject}: {mark}")

    
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    max_marks = 100 * len(subjects)
    obtained_marks = total_marks
    
    result_lines.append(f"Total Marks: {total_marks} / {max_marks}")
    result_lines.append(f"Obtained Marks: {obtained_marks}")
    result_lines.append(f"Average Marks: {average_marks:.2f}")

    result_card = [header, underline] + result_lines
    
    result_card_str = "\n".join(result_card)
    
    return result_card_str

def submit():
    student_name = entry_name.get()
    if not student_name:
        messagebox.showerror("Input Error", "Please enter the student's name")
        return

    marks = []
    for entry in entries:
        try:
            mark = int(entry.get())
            if mark < 0 or mark > 100:
                raise ValueError
            marks.append(mark)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid marks (0-100) for all subjects")
            return

    result_card = create_result_card(student_name, subjects, marks)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result_card)
    result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Result Card Generator")
root.configure(bg="#87CEEB")  

label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

tk.Label(root, text="Enter the student's name:", bg="#87CEEB", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(root, width=30, font=entry_font)
entry_name.grid(row=0, column=1, padx=10, pady=5)

subjects = ["Math-123", "Eletronics", "English", "Physics", "Chemistry"]
entries = []

tk.Label(root, text="Enter marks (0-100) for the following subjects:", bg="#87CEEB", font=label_font).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
for i, subject in enumerate(subjects):
    tk.Label(root, text=f"{subject}: ", bg="#87CEEB", font=label_font).grid(row=i+2, column=0, padx=10, pady=5, sticky=tk.W)
    entry = tk.Entry(root, width=5, font=entry_font)
    entry.grid(row=i+2, column=1, padx=10, pady=5, sticky=tk.W)
    entries.append(entry)

tk.Button(root, text="Show Result Card", command=submit, font=button_font, bg="#FFD700", activebackground="#FFA500").grid(row=len(subjects)+2, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, width=50, height=15, state=tk.DISABLED, font=("Helvetica", 12))
result_text.grid(row=len(subjects)+3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()



