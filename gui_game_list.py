import tkinter as tk
from tkinter import messagebox

def ans():
    total = 0
    correct_answers = ["shoaib akhtar", "python", "burj khalifa", "h++", "would"]
    user_answers = [ans1.get().lower(), ans2.get().lower(), ans3.get().lower(), ans4.get().lower(), ans5.get().lower()]

    for i in range(len(correct_answers)):
        if user_answers[i] == correct_answers[i]:
            total += 5

    messagebox.showinfo("Result", f"Your total points are {total}.")

app = tk.Tk()
app.title("Educational Quiz Application")
app.config(bg="lightblue")

canvas = tk.Canvas(app, bg="lightblue")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(app, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, bg="lightblue")
canvas.create_window((0, 0), window=frame, anchor='nw')

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
   
frame.bind("<Configure>", on_frame_configure)

tk.Label(frame, text="1. Guess the fastest bowler of the Pakistani cricket team?", bg="lightblue").grid(row=1,column=0, sticky=tk.W,padx=10, pady=10)
ans1 = tk.StringVar()
tk.Radiobutton(frame, text="Imran Khan", variable=ans1, value="Imran Khan", bg="lightblue").grid(row=2,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Babar Azam", variable=ans1, value="Babar Azam", bg="lightblue").grid(row=3,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Shoaib Akhtar", variable=ans1, value="Shoaib Akhtar", bg="lightblue").grid(row=4,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Rizwan", variable=ans1, value="Rizwan", bg="lightblue").grid(row=5,column=0, sticky=tk.W, padx=20)

tk.Label(frame, text="\n2. What is the most famous programming language?", bg="lightblue").grid(row=6,column=0, sticky=tk.W,padx=10, pady=10) 
ans2 = tk.StringVar()
tk.Radiobutton(frame, text="C#", variable=ans2, value="C#", bg="lightblue").grid(row=7,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="CSS", variable=ans2, value="CSS", bg="lightblue").grid(row=8,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Java", variable=ans2, value="Java", bg="lightblue").grid(row=9,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Python", variable=ans2, value="Python", bg="lightblue").grid(row=10,column=0, sticky=tk.W, padx=20)

tk.Label(frame, text="\n3. Which is the highest building in the world?", bg="lightblue").grid(row=11,column=0, sticky=tk.W,padx=10, pady=10)
ans3 = tk.StringVar()
tk.Radiobutton(frame, text="Heydar Aliyev Center", variable=ans3, value="Heydar Aliyev Center", bg="lightblue").grid(row=12,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Bilbao Guggenheim Museum", variable=ans3, value="Bilbao Guggenheim Museum", bg="lightblue").grid(row=13,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Burj Khalifa", variable=ans3, value="Burj Khalifa", bg="lightblue").grid(row=14,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Hagia Sophia", variable=ans3, value="Hagia Sophia", bg="lightblue").grid(row=15,column=0, sticky=tk.W, padx=20)

tk.Label(frame, text="\n4. Which one is not a programming language?", bg="lightblue").grid(row=16,column=0, sticky=tk.W,padx=10, pady=10)
ans4 = tk.StringVar()
tk.Radiobutton(frame, text="C#", variable=ans4, value="C#", bg="lightblue").grid(row=17,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Java", variable=ans4, value="Java", bg="lightblue").grid(row=18,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="Python", variable=ans4, value="Python", bg="lightblue").grid(row=19,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="H++", variable=ans4, value="H++", bg="lightblue").grid(row=20,column=0, sticky=tk.W, padx=20)

tk.Label(frame, text="\n5. If you had let me know earlier, I ___ have been able to come.", bg="lightblue").grid(row=21,column=0, sticky=tk.W,padx=10, pady=10)
ans5 = tk.StringVar()
tk.Radiobutton(frame, text="should", variable=ans5, value="should", bg="lightblue").grid(row=22,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="would", variable=ans5, value="would", bg="lightblue").grid(row=23,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="could", variable=ans5, value="could", bg="lightblue").grid(row=24,column=0, sticky=tk.W, padx=20)
tk.Radiobutton(frame, text="might", variable=ans5, value="might", bg="lightblue").grid(row=25,column=0, sticky=tk.W, padx=20)

tk.Button(frame, text="Submit", command=ans, bg="lightblue").grid(row=26,column=1,padx=10, pady=10)

app.mainloop()
