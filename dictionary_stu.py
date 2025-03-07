import tkinter as tk
from tkinter import messagebox

def view_students(students):
    if not students:
        messagebox.showinfo("View Students", "No students found.")
    else:
        students_info = "\n".join([f"Student: {name}, Score: {score}" for name, score in students.items()])
        messagebox.showinfo("View Students", students_info)

def add_student(students, name_entry, score_entry):
    name = name_entry.get()
    if name in students:
        messagebox.showerror("Error", "Student already exists.")
    else:
        score = score_entry.get()
        try:
            score = float(score)
            students[name] = score
            messagebox.showinfo("Success", "Student added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid score. Please enter a valid number.")
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

def remove_student(students, name_entry):
    name = name_entry.get()
    if name in students:
        del students[name]
        messagebox.showinfo("Success", "Student removed successfully.")
    else:
        messagebox.showerror("Error", "Student not found.")
    name_entry.delete(0, tk.END)

def search_student(students, name_entry):
    name = name_entry.get()
    if name in students:
        messagebox.showinfo("Student Found", f"Student: {name}, Score: {students[name]}")
    else:
        messagebox.showerror("Error", "Student not found.")
    name_entry.delete(0, tk.END)

def update_student_score(students, name_entry, score_entry):
    name = name_entry.get()
    if name in students:
        new_score = score_entry.get()
        try:
            new_score = float(new_score)
            students[name] = new_score
            messagebox.showinfo("Success", "Student score updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid score. Please enter a valid number.")
    else:
        messagebox.showerror("Error", "Student not found.")
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

def main():
    students = {}

    root = tk.Tk()
    root.title("Student Management System")

    root.configure(bg='#f0f0f0')

    name_label = tk.Label(root, text="Student Name:", bg='#f0f0f0', fg='#333333')
    name_label.grid(row=0, column=0, padx=10, pady=5)

    name_entry = tk.Entry(root, bg='white', fg='#333333', relief=tk.SOLID, bd=1)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    score_label = tk.Label(root, text="Student Total Marks:", bg='#f0f0f0', fg='#333333')
    score_label.grid(row=1, column=0, padx=10, pady=5)

    score_entry = tk.Entry(root, bg='white', fg='#333333', relief=tk.SOLID, bd=1)
    score_entry.grid(row=1, column=1, padx=10, pady=5)

    view_button = tk.Button(root, text="View Students", command=lambda: view_students(students), bg='#4caf50', fg='white', relief=tk.FLAT)
    view_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    add_button = tk.Button(root, text="Add Student", command=lambda: add_student(students, name_entry, score_entry), bg='#2196f3', fg='white', relief=tk.FLAT)
    add_button.grid(row=3, column=0, padx=10, pady=5)

    remove_button = tk.Button(root, text="Remove Student", command=lambda: remove_student(students, name_entry), bg='#f44336', fg='white', relief=tk.FLAT)
    remove_button.grid(row=3, column=1, padx=10, pady=5)

    search_button = tk.Button(root, text="Search Student", command=lambda: search_student(students, name_entry), bg='#ff9800', fg='white', relief=tk.FLAT)
    search_button.grid(row=4, column=0, padx=10, pady=5)

    update_button = tk.Button(root, text="Update Score", command=lambda: update_student_score(students, name_entry, score_entry), bg='#ffeb3b', fg='#333333', relief=tk.FLAT)
    update_button.grid(row=4, column=1, padx=10, pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, bg='#9e9e9e', fg='white', relief=tk.FLAT)
    exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
